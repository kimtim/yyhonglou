# generate_chapters_75_80_enhanced.py
import json
import zipfile
from pathlib import Path
import shutil

tmp_dir = Path("tmp_75_80_enhanced")
tmp_dir.mkdir(exist_ok=True)

# 🌟 第75–80回：rich relation with literary depth, symbolism, and psychological insight
raw_data = {
    "chapter75.json": [
        {"source": "贾母", "target": "中秋夜宴", "relation": "强撑欢颜赏月，闻远处悲音而叹：<cite class='quote'>这还不算，又添了这个！</cite>"},
        {"source": "尤氏", "target": "贾珍", "relation": "劝其收敛赌饮，反被讥‘装清白’；宁府淫佚已不可掩"},
        {"source": "甄家", "target": "抄家", "relation": "被抄后私寄财物至贾府，贾政忧惧：<cite class='quote'>祸必及身矣！</cite>"},
        {"source": "贾赦", "target": "贾环", "relation": "赞其诗‘有侯门气概’，暗贬宝玉‘终是不读书’"},
        {"source": "林黛玉", "target": "联句", "relation": "对月吟‘冷月葬花魂’，湘云接‘寒塘渡鹤影’，二人互惊其谶"},
        {"source": "妙玉", "target": "续诗", "relation": "深夜截稿，代作十三韵，叹道：<cite class='quote'>好诗！只是过于颓败凄楚。</cite>"}
    ],
    "chapter76.json": [
        {"source": "林黛玉", "target": "感伤", "relation": "因宝钗搬离、湘云将去，独倚栏杆垂泪：<cite class='quote'>人有聚就有散，聚时欢喜，到散时岂不清冷？</cite>"},
        {"source": "史湘云", "target": "宽慰", "relation": "邀黛玉联诗解闷，豪情中藏不舍：<cite class='quote'>你是个明白人，何必自苦如此？</cite>"},
        {"source": "凹晶馆", "target": "联句", "relation": "二人对月赋诗，‘寒塘渡鹤影，冷月葬花魂’成绝唱，妙玉突现截稿"},
        {"source": "妙玉", "target": "栊翠庵", "relation": "邀二人饮体己茶，论诗忌‘过悲’，实则自身亦陷孤寂"},
        {"source": "贾母", "target": "闻笛", "relation": "命吹笛助兴，笛声凄清，众人默然，盛筵将散之兆"}
    ],
    "chapter77.json": [
        {"source": "王夫人", "target": "晴雯之死", "relation": "闻其亡讯，冷言：<cite class='quote'>死了倒干净！</cite>毫无悔意"},
        {"source": "贾宝玉", "target": "芙蓉诔", "relation": "作《芙蓉女儿诔》祭晴雯，实为黛玉预悼：<cite class='quote'>茜纱窗下，我本无缘；黄土垄中，卿何薄命！</cite>"},
        {"source": "芳官等", "target": "水月庵", "relation": "被逐后削发为尼，智通、圆信诱骗入空门，实为贩卖"},
        {"source": "司棋", "target": "迎春", "relation": "跪求留下，迎春垂泪：‘我也没法子救你。’显其懦弱"},
        {"source": "王熙凤", "target": "病势", "relation": "血山崩复发，平儿忧心：‘只怕熬不过秋去。’"}
    ],
    "chapter78.json": [
        {"source": "贾宝玉", "target": "姽婳词", "relation": "奉父命作《姽婳词》颂林四娘，暗讽文官无能，武将忠烈"},
        {"source": "贾政", "target": "赞许", "relation": "罕见夸奖宝玉：<cite class='quote'>虽粗鄙，倒也有几分骨气。</cite>"},
        {"source": "林黛玉", "target": "改稿", "relation": "见《芙蓉诔》中‘红绡帐里’句，建议改为‘茜纱窗下’，宝玉顿悟其谶"},
        {"source": "薛蟠", "target": "夏金桂", "relation": "迎娶‘河东狮’，初尚畏惧，后渐受辖制"},
        {"source": "香菱", "target": "改名", "relation": "被夏金桂强令改名‘秋菱’，剥夺身份，埋下虐待伏笔"}
    ],
    "chapter79.json": [
        {"source": "夏金桂", "target": "香菱", "relation": "设局诬其勾引薛蟠，逼其改名，日夜折磨"},
        {"source": "薛姨妈", "target": "忍让", "relation": "劝香菱顺从：<cite class='quote'>她年轻，不知礼，你让着些。</cite>显薛家衰微"},
        {"source": "贾迎春", "target": "孙绍祖", "relation": "嫁‘中山狼’，婚后即遭凌辱，叹：<cite class='quote'>我不幸配了个冤家！</cite>"},
        {"source": "林黛玉", "target": "病重", "relation": "闻迎春婚变、香菱受虐，忧思成疾，咳血不止"},
        {"source": "贾宝玉", "target": "紫菱洲", "relation": "见迎春旧居荒凉，作歌悼念：<cite class='quote'>池塘一夜秋风冷，吹散芰荷红玉影。</cite>"}
    ],
    "chapter80.json": [
        {"source": "夏金桂", "target": "调唆", "relation": "挑拨薛蟠毒打香菱，又装病诬其下毒，手段阴狠"},
        {"source": "香菱", "target": "屈服", "relation": "被打后仍侍奉金桂，叹：<cite class='quote'>我原不该痴心妄想进大观园。</cite>理想彻底幻灭"},
        {"source": "王一贴", "target": "疗妒汤", "relation": "献‘疗妒汤’方：<cite class='quote'>一剂不效，吃十剂；十剂不效，吃百剂。</cite>实为讽刺"},
        {"source": "贾宝玉", "target": "天齐庙", "relation": "访道士问姻缘，闻‘金玉良缘’之说，心烦意乱"},
        {"source": "林黛玉", "target": "焚稿预兆", "relation": "病中整理诗帕，泪尽神伤，为后文‘焚稿断痴情’埋线"}
    ]
}

# 📜 高密度、高文学性的 summary（每回 ≥ 200字）
summaries = {
    75: "中秋夜，贾母强聚家人赏月，命吹笛助兴，却闻远处悲音，叹道：<cite class='quote'>这还不算，又添了这个！</cite>席间，贾赦赞贾环诗‘有侯门气概’，暗贬宝玉‘终是不读书’，父子嫌隙显露。尤氏劝贾珍收敛赌饮，反被讥‘装清白’，宁府淫佚已无可遮掩。更可怕者，甄家被抄后竟私寄财物至贾府，贾政忧惧：<cite class='quote'>祸必及身矣！</cite>此回以‘赏月’写‘末世’——月圆人不圆，家丑外扬，抄家阴影笼罩。黛玉、湘云于凹晶馆联句，‘寒塘渡鹤影，冷月葬花魂’互惊其谶，妙玉截稿续诗，叹其‘过于颓败凄楚’，实则三人心中皆知：繁华将尽，悲音已起。",
    
    76: "中秋后，宝钗搬离大观园，湘云亦将归家，黛玉独倚栏杆垂泪：<cite class='quote'>人有聚就有散，聚时欢喜，到散时岂不清冷？</cite>湘云邀其联诗解闷，二人至凹晶馆对月赋句，‘寒塘渡鹤影，冷月葬花魂’成千古绝唱，彼此惊觉此乃生死之谶。妙玉突现，邀入栊翠庵饮体己茶，代续十三韵，表面劝‘诗忌过悲’，实则自身亦陷‘槛外’孤寂。贾母命再吹笛，笛声凄清穿林，众人默然——此非欢宴，实为送别。此回以诗写命，以茶写隔，以笛写散，群芳星散之势已不可逆。",
    
    77: "晴雯病亡，王夫人闻讯冷言：<cite class='quote'>死了倒干净！</cite>毫无悔意。宝玉悲愤作《芙蓉女儿诔》，表面祭晴雯，实为黛玉预悼，中有句：<cite class='quote'>茜纱窗下，我本无缘；黄土垄中，卿何薄命！</cite>字字泣血。芳官、藕官等被逐后，智通、圆信假借佛门诱骗削发，实为贩卖人口。司棋跪求迎春相救，迎春垂泪：‘我也没法子救你。’显其‘懦小姐’本色。凤姐血山崩复发，平儿忧心：‘只怕熬不过秋去。’——至此，怡红院清净女儿世界彻底瓦解，主仆皆入绝境。",
    
    78: "贾政命宝玉作《姽婳词》颂林四娘殉国，宝玉借此暗讽文官无能、武将忠烈，贾政罕见赞许：<cite class='quote'>虽粗鄙，倒也有几分骨气。</cite>黛玉见《芙蓉诔》中‘红绡帐里’句，建议改为‘茜纱窗下’，宝玉顿悟此乃二人命运之谶，悚然而惊。与此同时，薛蟠迎娶夏金桂，初尚畏惧其悍，后渐受辖制。金桂强令香菱改名‘秋菱’，剥夺其‘香’字身份，埋下虐待伏笔。此回双线并进：一边是宝玉借古讽今的觉醒，一边是香菱理想世界的崩塌——‘香’变‘秋’，即是‘芬芳’被‘肃杀’取代。",
    
    79: "夏金桂设局诬香菱勾引薛蟠，逼其改名，日夜折磨。薛姨妈劝香菱：‘她年轻，不知礼，你让着些。’显薛家已无力护弱。迎春嫁‘中山狼’孙绍祖，婚后即遭凌辱，归宁时泣诉：<cite class='quote'>我不幸配了个冤家！</cite>宝玉至紫菱洲见其旧居荒凉，作歌悼念：<cite class='quote'>池塘一夜秋风冷，吹散芰荷红玉影。</cite>黛玉闻二女婚变，忧思成疾，咳血不止。此回写‘两桩婚姻，两种地狱’——一个被悍妇所制，一个被恶婿所虐，皆因父权包办、女性无权。黛玉之病，实为对姐妹命运的共感之痛。",
    
    80: "夏金桂挑拨薛蟠毒打香菱，又装病诬其下毒，手段阴狠至极。香菱被打后仍侍奉金桂，绝望叹道：<cite class='quote'>我原不该痴心妄想进大观园。</cite>其‘香菱梦’彻底幻灭。道士王一贴献‘疗妒汤’方：<cite class='quote'>一剂不效，吃十剂；十剂不效，吃百剂。</cite>实为辛辣讽刺——世间无药可医人性之恶。宝玉访天齐庙问姻缘，闻‘金玉良缘’之说，心烦意乱。黛玉病中整理旧日诗帕，泪尽神伤，默默焚稿之志已萌。至此，悲剧齿轮全面启动，只待最后一推。"
}

chapter_titles = {
    75: "第七十五回：开夜宴异兆发悲音 赏中秋新词得佳谶",
    76: "第七十六回：凸碧堂品笛感凄清 凹晶馆联诗悲寂寞",
    77: "第七十七回：俏丫鬟抱屈夭风流 美优伶斩情归水月",
    78: "第七十八回：老学士闲征姽婳词 痴公子杜撰芙蓉诔",
    79: "第七十九回：薛文龙悔娶河东狮 贾迎春误嫁中山狼",
    80: "第八十回：美香菱屈受贪夫棒 王道士胡诌妒妇方"
}

# 构建 JSON（确保 nodes 100% 覆盖）
for fname, links in raw_data.items():
    chap_num = int(fname.replace("chapter", "").replace(".json", ""))
    nodes_set = set()
    for link in links:
        nodes_set.add(link["source"])
        nodes_set.add(link["target"])
    nodes = sorted(nodes_set)
    
    content = {
        "title": chapter_titles[chap_num],
        "summary": summaries[chap_num],
        "nodes": nodes,
        "links": links
    }
    
    with open(tmp_dir / fname, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

# 🌟 极致详细的 appearances：事件 + 情感 + 功能 + 命运
characters_update = {
    "林黛玉": {
        "brief": "绛珠仙草，诗魂化身，情深命薄",
        "detail": "第75回联句‘冷月葬花魂’，自谶其死；第76回感聚散无常，垂泪独悲；第79回闻迎春、香菱婚变，忧思咳血；第80回整理诗帕，泪尽神伤，为‘焚稿断痴情’埋线。其病非身病，乃心病——眼见姐妹凋零，知自己亦难逃此劫。",
        "appearances": {
            "75": "联句‘冷月葬花魂’ → 互惊其谶（预感死亡）",
            "76": "感宝钗湘云离去 → 凹晶馆联诗 → 妙玉邀茶（孤独、清醒）",
            "79": "闻迎春婚变、香菱受虐 → 咳血（共感之痛）",
            "80": "整理诗帕 → 泪尽（决意断情，走向终局）"
        }
    },
    "香菱": {
        "brief": "甄英莲，命运多舛，曾怀‘入园梦’",
        "detail": "第78回被夏金桂强改名‘秋菱’，剥夺身份；第79–80回遭诬陷、毒打、下毒陷害，仍侍奉金桂，最终叹：‘我原不该痴心妄想进大观园。’其‘香’字被夺，象征纯洁被践踏，理想彻底幻灭。",
        "appearances": {
            "78": "被强改名‘秋菱’（身份剥夺）",
            "79": "遭诬勾引 → 被虐（恐惧、委屈）",
            "80": "被毒打 → 侍奉金桂 → 叹悔入园梦（绝望、屈服）"
        }
    },
    "贾宝玉": {
        "brief": "怡红公子，情不情，叛逆而无力",
        "detail": "第75回听悲音而默然；第77回作《芙蓉诔》祭晴雯，实悼黛玉；第78回作《姽婳词》暗讽时政；第79回悼迎春作歌；第80回问姻缘心乱。他愈觉醒，愈无力——眼见美好毁灭，却无法阻止。",
        "appearances": {
            "75": "闻悲音 → 默然（预感末世）",
            "77": "作《芙蓉诔》（深情、预悼）",
            "78": "作《姽婳词》→ 黛玉改稿（思想觉醒、命运顿悟）",
            "79": "悼迎春 → 作歌（悲悯、无力）",
            "80": "问姻缘 → 心烦（对‘金玉’宿命的抗拒）"
        }
    },
    "夏金桂": {
        "brief": "薛蟠妻，悍妒阴狠，‘河东狮’",
        "detail": "第78回入门即掌权；第79–80回设局诬香菱、逼改名、装病下毒，手段层层升级。她是封建婚姻中‘悍妇’的极端，也是男权社会对女性扭曲的产物——以恶制善，以妒杀人。",
        "appearances": {
            "78": "入门 → 掌控薛蟠（初显威势）",
            "79": "设局诬香菱 → 逼改名（心理摧残）",
            "80": "挑拨毒打 → 装病诬毒（肉体+精神双重虐待）"
        }
    },
    "妙玉": {
        "brief": "槛外人，高洁孤僻，实难超脱",
        "detail": "第75–76回截黛玉湘云联句，续十三韵，表面劝‘诗忌过悲’，实则自身亦陷孤寂。她以‘槛外’自居，却仍关心园中人事，其‘洁’与‘情’矛盾未解，预示日后‘终陷淖泥中’。",
        "appearances": {
            "75": "截稿续诗 → 叹‘过于颓败’（理性压抑情感）",
            "76": "邀饮体己茶 → 论诗（试图超脱，实则牵挂）"
        }
    }
}

with open(tmp_dir / "characters_update_75_80.json", "w", encoding="utf-8") as f:
    json.dump(characters_update, f, ensure_ascii=False, indent=2)

# 打包
zip_path = Path("chapters_75_80_relation_enhanced.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for p in tmp_dir.rglob("*"):
        zf.write(p, arcname=p.relative_to(tmp_dir))

shutil.rmtree(tmp_dir)

print("✅ 第75–80回 · TEXT-RICH ENHANCED 版生成完成！")
print("✨ relation：融入象征、心理、社会批判")
print("✨ summary：每回 ≥200字，多重<cite> + 主题点睛")
print("✨ appearances：事件+情感+功能+命运四维刻画")
print(f"📦 输出文件: {zip_path.resolve()}")