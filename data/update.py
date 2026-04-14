import json
from pathlib import Path

def update_characters(main_file: r'characters.json', patch_file: r'patches/update-1-5.json', output_file: str = None):
    """
    将 patch_file 中的人物数据增量合并到 main_file
    """
    # 加载主库与补丁
    with open(main_file, 'r', encoding='utf-8') as f:
        main_data = json.load(f)
    
    with open(patch_file, 'r', encoding='utf-8') as f:
        patch_data = json.load(f)

    updated = main_data.copy()

    for name, patch_info in patch_data.items():
        if name not in updated:
            # 新人物：直接加入
            updated[name] = patch_info
        else:
            # 已有人物：合并字段
            old = updated[name]
            
            # brief：保留非空最早的
            if not old.get("brief") and patch_info.get("brief"):
                old["brief"] = patch_info["brief"]
            
            # detail：保留更长的（通常更完整）
            old_detail = old.get("detail", "")
            new_detail = patch_info.get("detail", "")
            if len(new_detail) > len(old_detail):
                old["detail"] = new_detail
            
            # appearances：字典合并（新回目直接加，同回目可选择覆盖或拼接）
            old_appear = old.setdefault("appearances", {})
            new_appear = patch_info.get("appearances", {})
            for chap, event in new_appear.items():
                if chap in old_appear:
                    # 可选策略1：覆盖（假设新描述更准）
                    old_appear[chap] = event
                    # 可选策略2：拼接（保留所有细节）
                    # old_appear[chap] += "；" + event
                else:
                    old_appear[chap] = event

    # 输出
    out_path = output_file or main_file
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(updated, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已完成更新：{len(patch_data)} 条人物记录合并至 {out_path}")

# 使用示例
# 假设你已有 characters_main.json（可能是空或已有1-3回数据）
# update_characters("characters_main.json", "characters_update_01_05.json")