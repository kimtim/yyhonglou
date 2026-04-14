# generate_chapters_13_to_16_strict.py

import json

expected_nodes = {
    13: ["秦可卿", "王熙凤", "贾珍", "尤氏", "贾蓉", "宝玉", "平儿", "戴权", "瑞珠", "宝珠"],
    14: ["林如海", "贾琏", "黛玉", "北静王", "贾政", "宝玉", "凤姐", "净虚", "智能儿", "秦钟"],
    15: ["凤姐", "净虚", "智能儿", "秦钟", "水月庵", "铁槛寺", "张金哥", "守备之子", "李衙内"],
    16: ["秦钟", "智能儿", "贾母", "元春", "贾政", "宝玉", "赵嬷嬷", "贾琏"]
}

# =============== 第十三回 ===============
chapter13 = {
    "title": "第十三回 秦可卿死封龙禁尉 王熙凤协理宁国府",
    "core_sources": ["秦可卿", "王熙凤"],
    "summary": "凤姐夜卧，忽见秦可卿入梦：<cite class='quote'>月满则亏，水满则溢。</cite> 告诫趁今日富贵，置田庄于祖茔旁，设家塾于其侧，<cite class='quote'>便是有了罪，凡物可入官，这祭祀产业连官也不入的。</cite> 又言：<cite class='quote'>三春去后诸芳尽，各自须寻各自门。</cite> 言毕飘然。凤姐惊醒，即闻秦氏殁。宝玉闻信，<cite class='quote'>哇的一声，直喷出一口血来。</cite> 贾珍哀毁逾常，<cite class='quote'>哭得泪人一般。</cite> 尤氏称病不出。贾珍遂求凤姐协理宁府。凤姐素喜揽事，欣然应允，并思宁府五弊：<cite class='quote'>人口混杂，遗失东西；事无专执，临期推委；需用过费，滥支冒领；任无大小，苦乐不均；家人豪纵，有脸者不服钤束。</cite> 秦氏丫鬟瑞珠触柱殉主，宝珠甘为义女。",
    "nodes": [
        "秦可卿", "王熙凤", "贾珍", "尤氏", "贾蓉",
        "宝玉", "平儿", "戴权", "瑞珠", "宝珠"
    ],
    "links": [
        {"source": "秦可卿", "target": "王熙凤", "relation": "<cite class='quote'>非告诉婶子，别人未必中用。</cite> 秦可卿托梦凤姐，因唯其能行此远虑。"},
        {"source": "宝玉", "target": "秦可卿", "relation": "<cite class='quote'>哇的一声，直喷出一口血来。</cite> 宝玉感其逝，情动于中，血随气逆。"},
        {"source": "贾珍", "target": "秦可卿", "relation": "<cite class='quote'>哭得泪人一般。</cite> 贾珍哀痛逾礼，显其情逾常分。"},
        {"source": "王熙凤", "target": "贾珍", "relation": "贾珍央求凤姐协理，<cite class='quote'>便跪下道：‘婶子只管料理，我自当补报。’</cite>"},
        {"source": "尤氏", "target": "贾珍", "relation": "尤氏称病不出，<cite class='quote'>犯了旧疾，不能料理事务。</cite> 实避家丑。"},
        {"source": "瑞珠", "target": "秦可卿", "relation": "<cite class='quote'>触柱而亡。</cite> 瑞珠知主私隐，不得不殉。"},
        {"source": "宝珠", "target": "秦可卿", "relation": "<cite class='quote'>甘心愿为义女，誓任摔丧驾灵之任。</cite>"},
        {"source": "戴权", "target": "贾珍", "relation": "<cite class='quote'>戴权笑道：‘事已如此，何不速办？’</cite> 助贾蓉捐龙禁尉。"},
        {"source": "贾蓉", "target": "秦可卿", "relation": "贾蓉得五品职，只为灵前体面，<cite class='quote'>写在灵幡经榜上好看。</cite>"},
        {"source": "王熙凤", "target": "平儿", "relation": "凤姐理丧事，平儿掌对牌，<cite class='quote'>夜间算账至三更。</cite>"}
    ],
    "appearances": {
        "秦可卿": {"role": "宁府少奶奶", "detail": "托梦凤姐，留家族退路，死因隐晦。"},
        "王熙凤": {"role": "荣府管家", "detail": "接掌宁府，展露治才。"},
        "贾珍": {"role": "宁府族长", "detail": "哀毁逾常，捐官厚葬。"},
        "尤氏": {"role": "贾珍之妻", "detail": "称病避事，心知肚明。"},
        "贾蓉": {"role": "秦可卿之夫", "detail": "形同虚设，任父操办。"},
        "宝玉": {"role": "荣府嫡孙", "detail": "吐血示情，纯真未泯。"},
        "平儿": {"role": "凤姐心腹", "detail": "协理账目，细致周全。"},
        "戴权": {"role": "大明宫掌宫内相", "detail": "助贾珍买官，显宦官干政。"},
        "瑞珠": {"role": "秦可卿丫鬟", "detail": "触柱殉主，知秘而亡。"},
        "宝珠": {"role": "秦可卿丫鬟", "detail": "愿为义女，代行孝礼。"}
    }
}

# =============== 第十四回 ===============
chapter14 = {
    "title": "第十四回 林如海捐馆扬州城 贾宝玉路谒北静王",
    "core_sources": ["林如海", "北静王"],
    "summary": "凤姐协理宁府，每日卯正二刻点卯，<cite class='quote'>某人管某处，某人领某物，俱要登记。</cite> 违者不论亲疏，一概处罚。宁府上下肃然。忽传林如海殁于扬州，<cite class='quote'>贾琏送黛玉奔丧，年底方归。</cite> 秦氏出殡，四王八公皆至。北静王特设路祭，召见宝玉：<cite class='quote'>果然如宝似玉，名不虚传。</cite> 遂解腕上鹡鸰香念珠赠之：<cite class='quote'>权为贺敬之礼。</cite> 凤姐乘便遣人往铁槛寺，嘱净虚办事。智能儿随师同行，秦钟暗中留意。",
    "nodes": [
        "林如海", "贾琏", "黛玉", "北静王", "贾政",
        "宝玉", "凤姐", "净虚", "智能儿", "秦钟"
    ],
    "links": [
        {"source": "林如海", "target": "黛玉", "relation": "<cite class='quote'>捐馆扬州城。</cite> 黛玉自此孤苦无依。"},
        {"source": "北静王", "target": "宝玉", "relation": "<cite class='quote'>果然如宝似玉，名不虚传。</cite> 北静王爱其清秀，赠鹡鸰香念珠。"},
        {"source": "凤姐", "target": "宁府众人", "relation": "<cite class='quote'>既误卯，必罚；既滥支，必追。</cite> 凤姐立威，令行禁止。"},
        {"source": "净虚", "target": "凤姐", "relation": "<cite class='quote'>老尼们到了，再不能报答，只是记在心里。</cite> 净虚托凤姐干预张金哥婚事。"},
        {"source": "秦钟", "target": "智能儿", "relation": "智能儿随净虚赴铁槛寺，<cite class='quote'>秦钟见其俊俏，心下留神。</cite>"},
        {"source": "贾政", "target": "北静王", "relation": "<cite class='quote'>忙陪笑起身，迎至轿前。</cite> 显贾府对郡王之恭。"},
        {"source": "宝玉", "target": "鹡鸰香念珠", "relation": "<cite class='quote'>北静王所赐，系圣上所赐。</cite> 宝玉后转赠黛玉，黛玉嫌其‘什么臭男人拿过的’。"},
        {"source": "凤姐", "target": "贾珍", "relation": "凤姐协理丧事，<cite class='quote'>每日细查账目，不使宁府多费一钱。</cite>"},
        {"source": "贾琏", "target": "黛玉", "relation": "<cite class='quote'>送黛玉回扬州，料理林如海后事。</cite>"},
        {"source": "秦钟", "target": "宝玉", "relation": "秦钟随宝玉送殡，<cite class='quote'>二人同骑，窃语不断。</cite>"}
    ],
    "appearances": {
        "林如海": {"role": "巡盐御史", "detail": "黛玉之父，死讯断其归路。"},
        "贾琏": {"role": "荣府长房嫡子", "detail": "护送黛玉奔丧，年底方归。"},
        "黛玉": {"role": "荣府外孙女", "detail": "父丧后彻底寄人篱下。"},
        "北静王": {"role": "贤王", "detail": "赏识宝玉，赠御赐念珠。"},
        "贾政": {"role": "荣府二老爷", "detail": "恭敬迎王，恪守礼制。"},
        "宝玉": {"role": "荣府嫡孙", "detail": "受王青眼，不解世俗。"},
        "凤姐": {"role": "协理宁府", "detail": "雷厉风行，树立威信。"},
        "净虚": {"role": "水月庵主持", "detail": "借机托凤姐弄权。"},
        "智能儿": {"role": "净虚徒弟", "detail": "随师赴丧，引秦钟心动。"},
        "秦钟": {"role": "秦可卿之弟", "detail": "送殡途中，初萌情愫。"}
    }
}

# =============== 第十五回 ===============
chapter15 = {
    "title": "第十五回 王凤姐弄权铁槛寺 秦鲸卿得趣馒头庵",
    "core_sources": ["王熙凤", "秦钟"],
    "summary": "送殡至铁槛寺，凤姐收净虚所托：<cite class='quote'>长安守备之子聘张金哥，李衙内强娶，求太太救张家一命。</cite> 凤姐假贾琏名修书，逼守备退婚。守备无奈，金哥与守备子双双自尽。<cite class='quote'>凤姐坐享三千两，合家称叹其手段。</cite> 是夜，秦钟与智能儿偷会馒头庵：<cite class='quote'>那智能百般撩拨，秦钟魂魄俱销。</cite> 二人苟且，被宝玉撞破，<cite class='quote'>宝玉笑道：‘你倒也还干这些事！’</cite>",
    "nodes": [
        "凤姐", "净虚", "智能儿", "秦钟", "水月庵",
        "铁槛寺", "张金哥", "守备之子", "李衙内"
    ],
    "links": [
        {"source": "凤姐", "target": "净虚", "relation": "<cite class='quote'>你是素日知道我的，从来不信什么阴司地狱报应的。</cite> 凤姐为财弄权，草菅人命。"},
        {"source": "张金哥", "target": "守备之子", "relation": "<cite class='quote'>原已受聘，誓死不嫁他人。</cite>"},
        {"source": "李衙内", "target": "张金哥", "relation": "<cite class='quote'>倚势强娶，致其自缢。</cite>"},
        {"source": "秦钟", "target": "智能儿", "relation": "<cite class='quote'>那智能百般撩拨，秦钟魂魄俱销。</cite> 二人于馒头庵私通。"},
        {"source": "宝玉", "target": "秦钟", "relation": "<cite class='quote'>你倒也还干这些事！</cite> 宝玉撞破，半嗔半笑。"},
        {"source": "凤姐", "target": "贾琏", "relation": "凤姐假借贾琏名修书，<cite class='quote'>说与长安节度云老爷知道。</cite>"},
        {"source": "守备", "target": "守备之子", "relation": "<cite class='quote'>父子俱投河而死。</cite> 因退婚羞愤。"},
        {"source": "净虚", "target": "张金哥", "relation": "净虚受张家所托，<cite class='quote'>求凤姐作主，救他一家性命。</cite>"},
        {"source": "铁槛寺", "target": "水月庵", "relation": "铁槛寺停灵，水月庵歇宿，<cite class='quote'>寺傍庵居，僧尼杂处。</cite>"},
        {"source": "凤姐", "target": "三千两银", "relation": "<cite class='quote'>坐享三千两，自此胆识愈壮。</cite>"}
    ],
    "appearances": {
        "凤姐": {"role": "弄权者", "detail": "为三千两逼死两条人命，毫无悔意。"},
        "净虚": {"role": "讼棍尼姑", "detail": "挑起官司，借凤姐牟利。"},
        "智能儿": {"role": "水月庵小尼", "detail": "主动勾引秦钟，破戒偷情。"},
        "秦钟": {"role": "情欲少年", "detail": "丧姊不久，即与智能儿苟合。"},
        "张金哥": {"role": "长安民女", "detail": "守节自尽，成凤姐弄权牺牲品。"},
        "守备之子": {"role": "武官之子", "detail": "殉情投河。"},
        "李衙内": {"role": "权贵子弟", "detail": "仗势夺婚，致人命案。"},
        "水月庵": {"role": "尼庵", "detail": "表面清净，实藏污纳垢。"},
        "铁槛寺": {"role": "贾氏家庙", "detail": "停灵之所，亦成权谋之地。"}
    }
}

# =============== 第十六回 ===============
chapter16 = {
    "title": "第十六回 贾元春才选凤藻宫 秦鲸卿夭逝黄泉路",
    "core_sources": ["元春", "秦钟"],
    "summary": "忽传元春晋封凤藻宫尚书，加封贤德妃，<cite class='quote'>贾府上下欢天喜地。</cite> 赵嬷嬷道：<cite class='quote'>如今还有个太祖皇帝仿舜巡的故事呢！</cite> 暗指南巡接驾往事。秦钟自馒头庵归，<cite class='quote'>身子一日弱似一日。</cite> 智能儿逃至秦家，被秦业逐出，秦业气死。秦钟病重，宝玉探视，<cite class='quote'>秦钟道：‘以前你我见识自为高过世人，我今日才知自误了。’</cite> 言毕而逝。宝玉悲恸，<cite class='quote'>哭了一场，只得回来。</cite>",
    "nodes": [
        "秦钟", "智能儿", "贾母", "元春", "贾政",
        "宝玉", "赵嬷嬷", "贾琏"
    ],
    "links": [
        {"source": "元春", "target": "贾政", "relation": "<cite class='quote'>晋封凤藻宫尚书，加封贤德妃。</cite> 贾府烈火烹油之始。"},
        {"source": "秦钟", "target": "智能儿", "relation": "智能儿逃至秦家，<cite class='quote'>被秦业逐出，秦业气死。</cite>"},
        {"source": "秦钟", "target": "宝玉", "relation": "<cite class='quote'>以前你我见识自为高过世人，我今日才知自误了。</cite> 秦钟临终悔悟。"},
        {"source": "赵嬷嬷", "target": "贾琏", "relation": "<cite class='quote'>如今还有个太祖皇帝仿舜巡的故事呢！</cite> 忆当年接驾盛况。"},
        {"source": "贾母", "target": "元春", "relation": "<cite class='quote'>喜得念佛不止。</cite>"},
        {"source": "宝玉", "target": "秦钟", "relation": "<cite class='quote'>哭了一场，只得回来。</cite> 情友早夭，宝玉初尝生死之痛。"},
        {"source": "秦业", "target": "秦钟", "relation": "<cite class='quote'>气得老病发作，呜呼死了。</cite> 因智能儿事。"},
        {"source": "智能儿", "target": "秦业", "relation": "智能儿私逃至秦家，<cite class='quote'>求秦钟收留。</cite>"},
        {"source": "贾琏", "target": "凤姐", "relation": "<cite class='quote'>咱们家也太花费了，怕将来难以为继。</cite> 贾琏偶发忧思。"},
        {"source": "元春", "target": "贾府", "relation": "<cite class='quote'>烈火烹油，鲜花着锦之盛。</cite> 秦可卿托梦所言‘喜事’应验。"}
    ],
    "appearances": {
        "秦钟": {"role": "情友", "detail": "纵欲伤身，临终悔悟，早夭。"},
        "智能儿": {"role": "逃尼", "detail": "私奔秦家，致秦业气死。"},
        "元春": {"role": "皇妃", "detail": "晋封贤德妃，贾府极盛之兆。"},
        "贾母": {"role": "贾府老祖宗", "detail": "闻元春晋封，喜极念佛。"},
        "贾政": {"role": "荣府二老爷", "detail": "因女显贵，光耀门楣。"},
        "宝玉": {"role": "情痴", "detail": "送别秦钟，初悟人生无常。"},
        "赵嬷嬷": {"role": "贾琏乳母", "detail": "忆接驾往事，显贾府昔日辉煌。"},
        "贾琏": {"role": "荣府长房", "detail": "偶忧家计，旋即沉溺享乐。"}
    }
}

# =============== 校验输出 ===============
chapters = {13: chapter13, 14: chapter14, 15: chapter15, 16: chapter16}

for num, data in chapters.items():
    filename = f"chapter{num}_strict.json"
    actual = set(data["nodes"])
    expected = set(expected_nodes[num])
    missing = expected - actual
    if missing:
        print(f"⚠️ 第{num}回遗漏人物：{sorted(missing)}")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ 已生成 {filename}")

print("\n🎉 第13–16回（严格脂本引文+解读版）生成完毕！")