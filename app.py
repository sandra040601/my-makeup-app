import streamlit as st
import urllib.parse

# ==============================================================================
# 🗂️ 1. 永恆經典膚質資料庫 (依 500以下 / 500-1000 / 1000以上 嚴格分流)
# ==============================================================================
SKIN_DATABASE = {
    "oil": {
        "diagnosis": "【油性肌/痘痘肌學理診斷】\n臨床特徵為皮脂腺分泌過度旺盛。💡 產品挑選關鍵：應優先選擇含有『控油成分』或『酸類代謝成分』之清爽產品，避免毛孔阻塞。",
        "1": { # 💰 500元以下
            "step1_remover": {"reason": "開架萬年無油清爽卸妝水，天天大面積擦拭控油也不卡粉刺。", "items": ["【Biore 蜜妮】零油感舒敏卸妝水", "【妮維雅】B5精華卸妝水 控油淨透型", "【1028】深層潔淨卸妝水"]},
            "step2_cleanser": {"reason": "百元抗痘控油長青樹，微米泡沫深度洗淨毛孔油脂。", "items": ["【專科】超微米控油潔顏乳", "【曼秀雷敦】Acnes抗痘洗面乳", "【Biore 蜜妮】抗痘保濕洗面乳"]},
            "step3_toner": {"reason": "大容量高回購率清爽化妝水，二次清潔並調理粉刺角質。", "items": ["【Imju】薏仁清潤化妝水", "【自白肌】特濃玻尿酸保濕化妝水", "【專科】保濕專科化妝水(清爽型)"]},
            "step4_essence": {"reason": "小資界口碑純補水原液或精華，避開黏膩、強效控油調理。", "items": ["【TUNEMAKERS】甘草/原液保濕精華", "【達特醫】10%菸鹼醯胺精華液", "【Solone】補水控油噴霧精華"]},
            "step5_cream": {"reason": "百元清爽凝凍戰神，給予油肌最純粹的補水不補油。", "items": ["【雪芙蘭】水潤凝霜", "【Neutrogena 露得清】水活保濕凝露", "【肌研】極潤保濕水凝凍"]},
            "step6_sunscreen": {"reason": "平價不悶痘防曬，質地水感且迅速成膜，不泛油光。", "items": ["【曼秀雷敦】水潤肌超保濕水感防曬露", "【1028】超控油防曬隔離乳", "【Maybelline 媚比琳】反孔特霧防曬乳"]},
            "step7_base": {"reason": "開架蟬聯多年控油飾底乳霸主，完美吸附油脂、修飾毛孔。", "items": ["【SOFINA 漾緁】控油瓷效妝前隔離乳", "【1028】超控油飾底乳", "【媚點】零瑕美肌妝前乳(綠)"]},
            "step8_concealer": {"reason": "全球熱銷經典霧面遮瑕，質地偏乾，牢牢鎖死痘疤與局部泛紅。", "items": ["【Maybelline 媚比琳】FIT ME 遮瑕膏", "【heme】無瑕持久遮瑕蜜", "【1028】服服貼貼遮瑕膏"]},
            "step9_foundation": {"reason": "開架霧面粉底代名詞，持久耐汗，打造高級微霧妝效。", "items": ["【Maybelline 媚比琳】FIT ME 反孔特霧粉底液", "【KATE】零瑕肌密微霧粉底液", "【1028】極上鏡柔光超磁控粉底液"]},
            "step10_powder": {"reason": "小資必備萬年吸油蜜粉，一抹秒變柔焦霧面、徹底吸乾油光。", "items": ["【neuve 惹我】清爽吸油蜜粉", "【innisfree】無油無慮礦物控油蜜粉", "【1028】超吸油蜜粉餅"]},
            "step_eyebrow": {"reason": "抗油防水經典眉筆，不用擔心出油導致眉尾消失。", "items": ["【neuve 惹我】眉筆", "【Za】旋轉眉筆", "【1028】精算持色細眉筆"]},
            "step_contour": {"reason": "開架高CP值不致痘修容，純霧面不顯面部油光。", "items": ["【Solone】神隱修容餅", "【heme】三色修容餅", "【1028】輪廓定格好氣色雙妝盤"]}
        },
        "2": { # 💎 500～1000元
            "step1_remover": {"reason": "醫美頂級控油潔膚水始祖，深入毛孔洗淨油脂、配方長青。", "items": ["【BIODERMA 貝德瑪】淨妍控油潔膚液", "【理膚寶水】高效溫和卸妝水 控油型", "【雅漾】控油清爽潔膚水"]},
            "step2_cleanser": {"reason": "中階氨基酸或醫美控油潔顏，調理皮脂同時不破壞天然屏障。", "items": ["【Curel 珂潤】控油保濕洗顏慕斯", "【Dr.Wu】適肌控油潔顏慕斯", "【理膚寶水】深層控油泡沫洗面乳"]},
            "step3_toner": {"reason": "經典機能草本調理水，舒緩油痘泛紅、軟化粗糙角質。", "items": ["【Origins 品木宣言】青春無敵靈芝水", "【Labo Labo】毛孔緊緻化妝水", "【Kiehl's 契爾氏】金盞花植物精華化妝水"]},
            "step4_essence": {"reason": "含有長效水楊酸或果酸，深度淨化、調理毛孔並平衡油脂分泌。", "items": ["【寶拉珍選】2%水楊酸精華液", "【Dr.Wu】杏仁酸亮白煥膚精華", "【理膚寶水】淨痘無瑕極效精華 DUO+"]},
            "step5_cream": {"reason": "醫美級平衡控油乳液，有效抑制全天候面部多餘油脂。", "items": ["【理膚寶水】毛孔緊緻控油保濕乳", "【Vichy 薇姿】新皮脂平衡多效精華乳", "【雅漾】控油清爽保濕乳"]},
            "step6_sunscreen": {"reason": "醫美防曬最高防禦指標，超強抗油，成膜後絕不誘發痘痘發炎。", "items": ["【理膚寶水】全護清爽防曬液(清爽型)", "【Dr.Wu】全效控油防曬乳", "【雅漾】控油清爽防曬乳"]},
            "step7_base": {"reason": "網路長青持妝乳，控油保濕雙效兼具，全天防粉底暗沉。", "items": ["【Pony Effect】水透光控油妝前乳", "【MAQuillAGE 心機彩妝】星魅平衡持妝控油乳", "【Espoir】純素控油妝前乳"]},
            "step8_concealer": {"reason": "彩妝師必備高持久遮瑕，對抗油汗不易位移，完美隱形痘疤。", "items": ["【J/X】三色遮瑕膏", "【CLIO】無瑕持妝遮瑕膏", "【The Saem】完美遮瑕液盤"]},
            "step9_foundation": {"reason": "日系經典持久粉底，粉體細緻，完美貼合出油後的肌膚結構。", "items": ["【KATE】零瑕肌密持緞粉底液", "【CLIO】柔霧光澤持妝粉底液", "【Pony Effect】絕對遮瑕隱形粉底液"]},
            "step10_powder": {"reason": "各大討論區萬年熱推定妝噴霧，全天候維持霧面妝感。", "items": ["【KOSE 高絲】美顏定妝噴霧", "【I'M MEME】我愛油光除霧蜜粉餅", "【banila co】空氣感控油蜜粉"]},
            "step_eyebrow": {"reason": "台日神級砍刀眉筆，防汗防摩擦，新手老手盲買都不踩雷。", "items": ["【Excel】3合1持久造型眉筆", "【KATE】雙用立體眉筆", "【Dejavu】就是自然持色眉筆"]},
            "step_contour": {"reason": "正宗亞洲消腫灰棕調，粉質極致微粒子，打造超自然立體陰影。", "items": ["【M·A·C】時尚焦點小眼影 #Omega", "【Too Cool For School】美術課三色修容餅", "【Canmake】小臉雙色修容粉"]}
        },
        "3": { # 👑 1000元以上
            "step1_remover": {"reason": "頂級專櫃潔顏油王者，無人能敵的秒速乳化技術，卸妝兼深層養膚。", "items": ["【植村秀】黑米/抹茶精萃潔顏油", "【BOBBI BROWN】沁透茉莉淨妝油", "【CLINIQUE 倩碧】溫和卸妝膏"]},
            "step2_cleanser": {"reason": "奢華頂級氨基酸泡沫，溫和洗淨多餘皮脂，維持肌膚細緻洗感。", "items": ["【SK-II】全效活膚潔面乳", "【香奈兒】深海系列潔顏慕斯", "【DIOR】雪晶靈透亮潔顏乳"]},
            "step3_toner": {"reason": "專櫃神仙水代名詞，長效調理並強效提升肌膚油水平衡與透亮度。", "items": ["【SK-II】青春露", "【ESTEE LAUDER 雅詩蘭黛】微分子肌底原生露", "【LANCOME 蘭蔻】超極光活粹晶露"]},
            "step4_essence": {"reason": "全球修護精華永恆天王，強效穩健肌底、收斂粗大毛孔、瑕疵不留痕。", "items": ["【蘭蔻】超未來肌因賦活露(小黑瓶)", "【雅詩蘭黛】特潤超導修護露(小棕瓶)", "【修麗可】果酸全面調理精華"]},
            "step5_cream": {"reason": "專櫃吸油明星水凝凍，24小時強效鎖水且膚感極致輕盈無負擔。", "items": ["【Kiehl's 契爾氏】冰河醣蛋白吸油水凝凍", "【CLINIQUE 倩碧】水磁場100H活水循環凝膠", "【BIOTHERM 碧兒泉】極量控油水凝凍"]},
            "step6_sunscreen": {"reason": "專櫃頂級抗老防曬，高滲透成膜技術，完全不油悶、完美阻絕紫外線。", "items": ["【肌膚之鑰】無瑕防曬護膚膏", "【LANCOME 蘭蔻】超輕盈UV水凝露", "【SHISEIDO 資生堂】防曬無油防護乳"]},
            "step7_base": {"reason": "神級妝前控油打底，瞬間平滑肌膚毛孔，神級對抗中東油田。", "items": ["【YSL】名模肌密光燦水凝露", "【M·A·C】超顯白持妝乳", "【GIVENCHY】高級訂製妝前打底乳"]},
            "step8_concealer": {"reason": "奢華不卡紋高粉體遮瑕，一抹完美霧化痘痘，兼具極致貼膚延展度。", "items": ["【NARS】奢華絲柔持妝遮瑕霜", "【肌膚之鑰】皆效無瑕遮瑕膏", "【DIOR】超完美持久遮瑕乳"]},
            "step9_foundation": {"reason": "抗油抗汗粉底液的絕對霸主，超強控油遇汗更美麗，專櫃油肌終極救星。", "items": ["【雅詩蘭黛】粉持久完美持妝粉底", "【植村秀】無極限超時輕粉底", "【YSL】恆久完美無瑕持妝粉底"]},
            "step10_powder": {"reason": "專業彩妝師人手一罐的煙霧級蜜粉，長效鎖死油光、全面柔焦毛孔。", "items": ["【LAURA MERCIER 蘿拉蜜思】煥顏透明蜜粉", "【M·A·C】超持妝輕透鏡蜜粉", "【GIVENCHY】高級訂製四格蜜粉"]},
            "step_eyebrow": {"reason": "殿堂級自動武士刀眉筆，只在有毛髮油脂處發色，抗汗持色極限。", "items": ["【植村秀】自動武士刀眉筆", "【肌膚之鑰】線條美眉筆", "【DIOR】搶眼造型眉筆"]},
            "step_contour": {"reason": "專櫃銷售冠軍修容與腮紅，完美貼合雙頰，創造頂級精緻深邃骨相。", "items": ["【NARS】3D立體燦光修容餅", "【NARS】炫色腮紅", "【Fenty Beauty】琥珀修容棒"]}
        }
    },
    "dry": {
        "diagnosis": "【乾燥肌/缺水肌學理診斷】\n臨床特徵為角質層含水量屏障受損。💡 產品挑選關鍵：必須優先選擇含有『高保濕因子』或『親膚性植物油』的潤澤型產品，避免乾裂卡粉。",
        "1": { # 💰 500元以下
            "step1_remover": {"reason": "平價潤澤卸妝乳，質地滑順減少摩擦，且不帶走乾肌天然油脂。", "items": ["【Biore 蜜妮】深層卸妝乳", "【Pond's 旁氏】冷霜卸妝膏", "【妮維雅】保濕深層卸妝乳"]},
            "step2_cleanser": {"reason": "高濃度玻尿酸保濕洗面乳，洗後臉部水嫩彈潤、完全不乾澀緊繃。", "items": ["【肌研】極潤保濕洗面乳", "【專科】超微米保濕潔顏乳", "【雪芙蘭】胺基酸保濕洗面乳"]},
            "step3_toner": {"reason": "保濕化妝水鼻祖，多重玻尿酸強效補水，瞬間滋潤乾燥角質層。", "items": ["【肌研】極潤保濕化妝水", "【Avene 雅漾】舒護活泉水", "【MINON】豐潤保濕化妝水"]},
            "step4_essence": {"reason": "基礎小資補水精華，密集修護乾燥引起的細紋與緊繃感。", "items": ["【L'Oreal 巴黎萊雅】玻尿酸瞬效保濕精華", "【Neogence 霓淨思】玻尿酸保濕精華液", "【Solone】密集補水精華液"]},
            "step5_cream": {"reason": "百年經典大藍罐，豐富封閉性油脂成分，築起最強防乾裂厚膜。", "items": ["【NIVEA 妮維雅】妮維雅霜(藍罐)", "【雪芙蘭】滋養霜 經典保濕", "【CeraVe 適樂膚】長效潤澤修護乳"]},
            "step6_sunscreen": {"reason": "水感精華防曬啫喱，保曬同時兼顧全天候肌膚水潤透亮感。", "items": ["【Canmake】美人魚防曬啫喱", "【雪芙蘭】超水感保濕防曬凝乳", "【專科】完美防曬水凝乳"]},
            "step7_base": {"reason": "高比例保濕成分打底，瞬間融入乾燥肌底、防止後續乾裂。", "items": ["【CEZANNE】長效保濕妝前乳", "【Media 媚點】保濕礦物妝前乳", "【SOFINA 漾緁】水潤瓷效妝前乳"]},
            "step8_concealer": {"reason": "水潤不卡紋遮瑕，完美修飾黑眼圈與眼周乾燥區，絕不卡粉。", "items": ["【Maybelline 媚比琳】FIT ME 遮瑕膏", "【1028】服服貼貼遮瑕膏", "【The Saem】重點遮瑕液"]},
            "step9_foundation": {"reason": "高保濕礦物粉底霜，為乾燥、脫屑肌膚注入滿滿奶油水光。", "items": ["【Media 媚點】粉嫩保濕礦物粉底霜", "【INTEGRATE】迷人光采粉底精華", "【Kate】柔焦瑕力粉底液"]},
            "step10_powder": {"reason": "以高細緻保濕定妝噴霧代替蜜粉，緊鎖水分，杜絕全臉起皮。", "items": ["【1028】空氣定妝噴霧(保濕型)", "【高絲】美顏定妝噴霧保濕版", "【卡羅美】持久保濕定妝噴霧"]},
            "step_eyebrow": {"reason": "滑順微發色眉筆，即使眉骨乾燥乾燥也能溫和流暢上色。", "items": ["【Solone】天生好手極細三角眉筆", "【heme】極細持色眉筆", "【Za】旋轉眉筆"]},
            "step_contour": {"reason": "貼膚度極佳的經典開架壓粉，柔和修飾雙頰不顯乾燥皮屑。", "items": ["【heme】純色腮紅 #04", "【Solone】神隱修容餅", "【CEZANNE】小臉修容餅"]}
        },
        "2": { # 💎 500～1000元
            "step1_remover": {"reason": "醫美低敏滋潤卸妝，溫和不刺激，守護乾肌關鍵神經醯胺。", "items": ["【Curel 珂潤】潤浸保濕卸妝凝露", "【舒特膚】溫和卸妝乳", "【理膚寶水】溫和保濕卸妝乳"]},
            "step2_cleanser": {"reason": "萬年熱銷不含皂鹼洗顏，乾性敏弱肌洗後的極致不緊繃享受。", "items": ["【Cetaphil 舒特膚】溫和潔膚乳", "【Curel 珂潤】潤浸保濕洗顏慕斯", "【理膚寶水】玻尿酸保濕洗面乳"]},
            "step3_toner": {"reason": "專門神經醯胺前導保濕水，迅速抓水、全面穩健脆弱角質層。", "items": ["【Curel 珂潤】潤浸保濕化妝水", "【Dr.Wu】玻尿酸保濕精華化妝水", "【TUNEMAKERS】神經醯胺前導保濕水"]},
            "step4_essence": {"reason": "經典醫美 B5 天王，深度補水修護，一抹消除雙頰粗糙乾紋。", "items": ["【理膚寶水】B5彈潤修復精華", "【Dr.Wu】玻學派維他命B5保濕精華", "【Neogence 霓淨思】積雪草B5修護純粹精華"]},
            "step5_cream": {"reason": "各大美妝賞萬年第一名的神級乳霜，滋潤不黏，防乾皮起屑王者。", "items": ["【Curel 珂潤】潤浸保濕深層乳霜", "【CeraVe 適樂膚】長效潤澤修護霜", "【理膚寶水】多容安極效舒緩修護乳"]},
            "step6_sunscreen": {"reason": "醫美級高保濕物理防曬，全面折射紫外線同時滋潤乾燥表皮。", "items": ["【理膚寶水】全護長效保濕防曬乳", "【Curel 珂潤】潤浸保濕防曬乳", "【Dr.Wu】全效保濕防曬乳"]},
            "step7_base": {"reason": "爆水級經典妝前，提供極高保濕度，維持全天底妝水潤服貼。", "items": ["【Pony Effect】水透光妝前防護乳", "【Excel】柔采光透妝前乳", "【KATE】零瑕肌密濾鏡妝前乳(保濕)"]},
            "step8_concealer": {"reason": "高延展性保濕修護遮瑕膏，絕不乾裂卡粉，完美隱形黑眼圈。", "items": ["【Medicube】修護遮瑕液", "【d program 敏感話題】敏弱遮瑕膏", "【CLIO】無瑕水潤遮瑕蜜"]},
            "step9_foundation": {"reason": "兼具高潤澤感與精緻透亮奶油光的保濕型粉底液。", "items": ["【CLIO】柔霧光澤水感粉底液", "【Maybelline 媚比琳】FIT ME水潤透亮粉底液", "【1028】極上鏡柔光超磁控粉底液(保濕版)"]},
            "step10_powder": {"reason": "口碑第一的長效保濕成膜定妝噴霧，緊鎖水分防止起皮脫妝。", "items": ["【Pony Effect】絕對持久定妝噴霧", "【高絲】高絲美顏定妝噴霧", "【SOFINA 漾緁】水潤定妝噴霧"]},
            "step_eyebrow": {"reason": "台日大受歡迎的三合一眉筆，添加滋潤蠟質、滑順不易扯皮。", "items": ["【Excel】3合1持久造型眉筆", "【KATE】雙用立體眉筆", "【Clio】不暈染極細自動眉筆"]},
            "step_contour": {"reason": "添加植物精華滋潤成分的日系打亮修容，完美貼合乾燥雙頰。", "items": ["【Canmake】小臉修容餅", "【Rimmel 倫敦荒漠】持久修容盤", "【3CE】立體雙色修容盤"]}
        },
        "3": { # 👑 1000元以上
            "step1_remover": {"reason": "貴婦級養膚型卸妝始祖，膏體化為親膚油脂，帶來頂級滋潤感。", "items": ["【EVE LOM】全能深層潔淨霜", "【DARPHIN 花梨木】按摩潔面膏", "【BOBBI BROWN】沁透茉莉淨妝油"]},
            "step2_cleanser": {"reason": "貴婦專櫃胺基酸洗面乳，富含養膚成分，洗後膚感絲滑柔嫩。", "items": ["【香奈兒】深海系列潔顏慕斯", "【肌膚之鑰】精萃光采潔膚皂", "【SUQQU】絕緻晶艷潤膚潔面乳"]},
            "step3_toner": {"reason": "高奢玫瑰/濃縮精華水，高滲透力瞬間為乾肌提供最奢華的滋養。", "items": ["【LANCOME 蘭蔻】絕對完美玫瑰修護露", "【LA MER 海洋拉娜】濃縮精華露", "【SHISEIDO 資生堂】紅色活酵超導奇蹟露"]},
            "step4_essence": {"reason": "殿堂級修護精華雙子星，強效穩健皮膚物理屏障，全面告別粗糙。", "items": ["【蘭蔻】超未來肌因賦活露(小黑瓶)", "【雅詩蘭黛】特潤超導修護露(小棕瓶)", "【香奈兒】山茶花保濕微導入精華液"]},
            "step5_cream": {"reason": "三十年傳奇暢銷百優精純乳霜，深度滋養，強效阻斷乾紋。", "items": ["【SHISEIDO 資生堂】百優精純乳霜", "【海洋拉娜】經典乳霜", "【Kiehl's 契爾氏】冰河醣蛋白保濕霜"]},
            "step6_sunscreen": {"reason": "頂級奢華保養級全效防曬，極高含水量，打造精緻上妝底層。", "items": ["【肌膚之鑰】全效防護乳", "【CHANEL】珍珠光感超淨化防護乳", "【DIOR】雪晶靈輕透防曬隔離乳"]},
            "step7_base": {"reason": "貴婦圈必備長管隔離霜，瞬間撫平乾燥紋理，煥發精緻貴婦光澤。", "items": ["【肌膚之鑰】光采無瑕妝前凝霜", "【蘿拉蜜思】煥顏凝露保濕型", "【PAUL & JOE】糖瓷絲潤隔離乳"]},
            "step8_concealer": {"reason": "奢華養膚冬蟲夏草遮瑕，極致輕盈貼膚，完全隱形眼周乾紋。", "items": ["【BOBBI BROWN】冬蟲夏草奢華遮瑕膏", "【肌膚之鑰】皆效無瑕遮瑕膏", "【LA MER 海洋拉娜】奇蹟煥采遮瑕膏"]},
            "step9_foundation": {"reason": "頂級養膚精華粉底始祖，注入滿滿保養精華，打造貴婦水光肌。", "items": ["【BOBBI BROWN】冬蟲夏草精華粉底", "【LANCOME 蘭蔻】絕對完美粉底精粹", "【SUQQU】絕緻艷澤粉霜"]},
            "step10_powder": {"reason": "專櫃奢華極細乾粉，定妝完美柔焦，且絕不奪走肌膚任何水分。", "items": ["【香奈兒】輕盈完美蜜粉", "【肌膚之鑰】光采蜜粉", "【SUQQU】晶采透霧蜜粉"]},
            "step_eyebrow": {"reason": "滑順絲絨質感的殿堂級專櫃眉筆，不拉扯乾燥脆弱的眼周。", "items": ["【植村秀】自動武士刀眉筆", "【TOM FORD】巨星三合一塑型眉筆", "【香奈兒】持久防水眉筆"]},
            "step_contour": {"reason": "頂級細緻粉體打亮修容，一抹平滑不顯肌膚乾紋，創造神級深邃光影。", "items": ["【肌膚之鑰】立體打亮修容盤", "【BOBBI BROWN】飛霞修容餅", "【Kevyn Aucoin】修容餅"]}
        }
    },
    "mix": {
        "diagnosis": "【混合肌學理診斷】\n面部皮脂腺分布不均，T字部位出油旺盛而雙頰乾燥緊繃。💡 產品挑選關鍵：應選擇具有『水油平衡調節』能力或採取『分區保養底妝』策略。",
        "1": { # 💰 500元以下
            "step1_remover": {"reason": "溫和、清爽且大容量的開架平衡潔膚水，全臉零黏膩感。", "items": ["【妮維雅】零油感保濕卸妝水", "【Biore 蜜妮】溫和卸妝乳", "【貝德瑪】舒敏潔膚液小資版"]},
            "step2_cleanser": {"reason": "日系高回購水油平衡潔顏，洗後雙頰潤澤、T字清爽。", "items": ["【Biore 蜜妮】溫和水嫩洗面乳", "【專科】保濕控油洗面乳", "【雪芙蘭】水肌精保濕洗面乳"]},
            "step3_toner": {"reason": "純補水、配方萬年不變，既不讓 T 字黏悶，又能適度滋潤雙頰。", "items": ["【Imju】薏仁清潤化妝水", "【肌研】極潤保濕化妝水", "【獨島】1025獨島化妝水"]},
            "step4_essence": {"reason": "小資界明星玻尿酸精華，質地極度輕盈，讓全臉無負擔。", "items": ["【Neogence 霓淨思】玻尿酸保濕精華液", "【L'Oreal 巴黎萊雅】玻尿酸瞬效保濕精華", "【Solone】玻尿酸保濕精華"]},
            "step5_cream": {"reason": "輕盈水凝霜代表，給予雙頰足夠鎖水力、又不易悶長 T 字粉刺。", "items": ["【雪芙蘭】水潤凝霜", "【Neutrogena 露得清】水活保濕凝露", "【CeraVe 適樂膚】全效超級保濕乳"]},
            "step6_sunscreen": {"reason": "長年穩坐開架前三名水感防曬，全臉推勻快速成膜，零負擔。", "items": ["【曼秀雷敦】水潤肌超保濕水感防曬露", "【妮維雅】三重防護輕感防曬凝乳", "【Biore 蜜妮】含水防曬清透水凝露"]},
            "step7_base": {"reason": "人手一瓶的開架控油妝前始祖，完美分區按壓 T 字、防止脫妝。", "items": ["【SOFINA 漾緁】控油瓷效妝前隔離乳", "【1028】超控油飾底乳", "【媚點】防曬妝前乳"]},
            "step8_concealer": {"reason": "全球暢銷高平衡度遮瑕，完美過渡出油區與乾燥區的色差。", "items": ["【Maybelline 媚比琳】FIT ME 遮瑕膏", "【1028】服服貼貼遮瑕膏", "【heme】無瑕持久遮瑕蜜"]},
            "step9_foundation": {"reason": "開架超人氣粉底，水潤好推不卡乾紋，對雙頰友善且兼具 T 字抗汗力。", "items": ["【Maybelline 媚比琳】FIT ME 反孔特霧粉底液", "【Media 媚點】自然肌透持效粉底液", "【INTEGRATE】柔焦輕透美肌粉底液"]},
            "step10_powder": {"reason": "百元神級按壓吸油蜜粉，專攻 T字部位吸附油脂、雙頰輕輕帶過。", "items": ["【neuve 惹我】清爽吸油蜜粉", "【1028】超吸油蜜粉餅", "【innisfree】無油無慮礦物控油蜜粉"]},
            "step_eyebrow": {"reason": "筆芯滑順、軟硬適中，完美因應混合肌面部油脂不均。", "items": ["【neuve 惹我】眉筆", "【Za】旋轉眉筆", "【1028】我型我塑持色眉筆"]},
            "step_contour": {"reason": "台灣高質感三色修容，T字不顯油光、雙頰不過度乾燥。", "items": ["【heme】三色修容餅", "【Solone】神隱修容餅", "【1028】輪廓定格雙妝盤"]}
        },
        "2": { # 💎 500～1000元
            "step1_remover": {"reason": "經典醫美霸主全能潔膚液，高效溫和，洗後全臉水油膚感極致平衡。", "items": ["【BIODERMA 貝德瑪】舒敏潔膚液", "【理膚寶水】高效溫和卸妝水", "【雅漾】舒敏卸妝潔膚水"]},
            "step2_cleanser": {"reason": "氨基酸溫和水油平衡慕斯，洗後雙頰潤澤、T字控油清爽。", "items": ["【Curel 珂潤】潤浸保濕洗顏慕斯", "【Dr.Wu】開架升級潔顏慕斯", "【Cetaphil 舒特膚】溫和舒敏洗顏慕斯"]},
            "step3_toner": {"reason": "經典機能調理水，穩定混合肌換季、失衡與粗糙膚況的首選。", "items": ["【Origins 品木宣言】青春無敵靈芝水", "【IPSA】美膚微整機能液流金水", "【Kiehl's 契爾氏】金盞花植物精華化妝水"]},
            "step4_essence": {"reason": "長年穩占核心地位的醫美B5精華，讓油水結構趨於健康穩定。", "items": ["【理膚寶水】B5彈潤修復精華", "【Dr.Wu】玻學派維他命B5保濕精華", "【Neogence 霓淨思】積雪草B5修護純粹精華"]},
            "step5_cream": {"reason": "補水不補油的清爽凝凍大師，完美修護雙頰、全天候清爽。", "items": ["【Kiehl's 契爾氏】冰河醣蛋白無油清爽凝凍", "【理膚寶水】毛孔緊緻控油保濕乳", "【Clinique 倩碧】水磁場72H保濕凝膠"]},
            "step6_sunscreen": {"reason": "護膚級醫美高防禦防曬，成膜快、不致粉刺、分區防禦老化。", "items": ["【理膚寶水】全護清爽防曬液", "【Dr.Wu】全效保濕防曬乳", "【雅漾】全效抗UV物理防曬乳"]},
            "step7_base": {"reason": "日系與韓系長青持妝乳，平衡全臉水油分布，不乾燥、不浮油。", "items": ["【MAQuillAGE 心機彩妝】心機平衡持妝乳", "【KATE】零瑕肌密持妝乳", "【Pony Effect】水透光妝前乳"]},
            "step8_concealer": {"reason": "經典熱銷三色遮瑕盤，可依各區域乾燥/出油程度自由調配滋潤度。", "items": ["【J/X】三色遮瑕膏", "【Excel】完美全效遮瑕盤", "【CLIO】無瑕持妝遮瑕膏"]},
            "step9_foundation": {"reason": "微霧面偏緞面質地明星粉底，完美隱形 T 字毛孔且服貼雙頰。", "items": ["【KATE】零瑕肌密微霧粉底液", "【CLIO】柔霧光澤持妝粉底液", "【Maybelline 媚比琳】反孔特霧粉底液"]},
            "step10_powder": {"reason": "各大討論區萬年熱推定妝噴霧，完美鎖住全臉不同區塊的精緻妝容。", "items": ["【KOSE 高絲】美顏定妝噴霧", "【Pony Effect】絕對持久定妝噴霧", "【1028】空氣定妝噴霧"]},
            "step_eyebrow": {"reason": "高人氣三合一眉筆，集眉筆、眉粉、眉刷於一身，持色力強。", "items": ["【Excel】3合1持久造型眉筆", "【KATE】雙用立體眉筆", "【Innisfree】妝自然眉筆"]},
            "step_contour": {"reason": "韓系經典國民三色修容，灰調不發紅，最適合混合肌打造精緻鼻影。", "items": ["【Too Cool For School】美術課三色修容餅", "【Romand】設計師雙色修容", "【I'M MEME】我愛修容魔術棒"]}
        },
        "3": { # 👑 1000元以上
            "step1_remover": {"reason": "專櫃頂級潔顏油王者，深入毛孔乳化，全臉洗後膚感極致平衡。", "items": ["【植村秀】抹茶/黑米精萃潔顏油", "【THREE】平衡潔膚油", "【BOBBI BROWN】沁透茉莉淨妝油"]},
            "step2_cleanser": {"reason": "天然高奢洗顏，溫和調理並洗淨面部不同區塊皮脂結構。", "items": ["【SK-II】全效活膚潔面乳", "【香奈兒】深海系列潔顏慕斯", "【THREE】平衡潔膚蜜"]},
            "step3_toner": {"reason": "風靡數十年的專櫃神仙水，全面深層調理並強效平衡油水分泌。", "items": ["【SK-II】青春露", "【ESTEE LAUDER 雅詩蘭黛】微分子肌底原生露", "【LANCOME 蘭蔻】超極光活粹晶露"]},
            "step4_essence": {"reason": "專櫃修護精華雙子星，調控T字皮脂同時深層修護雙頰乾燥脫屑。", "items": ["【蘭蔻】超未來肌因賦活露(小黑瓶)", "【雅詩蘭黛】特潤超導修護露(小棕瓶)", "【香奈兒】山茶花保濕微導入精華液"]},
            "step5_cream": {"reason": "高奢輕盈型專櫃水凝乳，輕盈鎖水、提供極致分區水分調控。", "items": ["【倩碧】水磁場100H活水循環凝膠", "【Kiehl's 契爾氏】冰河醣蛋白吸油水凝凍", "【LANCOME 蘭蔻】超輕盈雪紡水凝乳"]},
            "step6_sunscreen": {"reason": "奢華清爽抗老防曬代表，高滲透成膜技術，全臉輕透無負擔。", "items": ["【肌膚之鑰】無瑕防曬護膚膏", "【LANCOME 蘭蔻】超輕盈UV水凝露", "【CHANEL】珍珠光感超淨化防護乳"]},
            "step7_base": {"reason": "專櫃級爆水持妝乳，保濕度絕對足夠，且強效對抗T字出油。", "items": ["【植村秀】無極限保濕妝前乳", "【YSL】名模肌密光燦水凝露", "【M·A·C】超顯白持妝乳"]},
            "step8_concealer": {"reason": "頂級高粉體輕盈遮瑕，瞬間霧化T字毛孔並滋潤雙頰暗沉。", "items": ["【NARS】奢華絲柔持妝遮瑕霜", "【DIOR】超完美持久遮瑕乳", "【肌膚之鑰】皆效無瑕遮瑕膏"]},
            "step9_foundation": {"reason": "動態感應持妝科技粉底，面部遇油時更加持妝、遇乾燥時自動補水。", "items": ["【SHISEIDO 資生堂】超進化持久粉底液", "【雅詩蘭黛】粉持久完美持妝粉底", "【植村秀】無極限超時輕粉底"]},
            "step10_powder": {"reason": "專櫃經典透明蜜粉始祖，長效控制T字油光，且雙頰絕不乾裂起皮。", "items": ["【LAURA MERCIER 蘿拉蜜思】煥顏透明蜜粉", "【M·A·C】超持妝輕透鏡蜜粉", "【GIVENCHY】高級訂製裝四格蜜粉"]},
            "step_eyebrow": {"reason": "神級殿堂武士刀筆芯，抗全臉油水，精細描繪野生眉流感。", "items": ["【植村秀】自動武士刀眉筆", "【BOBBI BROWN】超防水斜角眉筆", "【Suqqu】晶采柔飾眉筆"]},
            "step_contour": {"reason": "亞洲消腫灰調大師，完美打造 T 字挺拔與雙頰立體光影。", "items": ["【M·A·C】時尚焦點小眼影 #Omega", "【KA】神級修容餅 #Medium", "【CHANEL】時尚雙色修容盤"]}
        }
    },
    "sensitive": {
        "diagnosis": "【敏感肌/泛紅肌學理診斷】\n皮膚物理性與化學性屏障功能嚴重受損。💡 產品挑選關鍵：應嚴格遵循『極簡成分與無刺激學理』，底妝避開酒精、香料、高濃度化學防曬，優先選用物理防曬與礦物成分。",
        "1": { # 💰 500元以下
            "step1_remover": {"reason": "開架純植物性成分基底卸妝，大幅減少界面活性劑的物理刺激。", "items": ["【無印良品】敏感肌卸妝油", "【Biore 蜜妮】溫和保濕卸妝乳", "【貝德瑪】舒敏潔膚液小容量版"]},
            "step2_cleanser": {"reason": "無香料酒精、不含皂鹼，超低刺激性，溫和清潔泛紅面部。", "items": ["【舒特膚】溫和潔膚乳", "【無印良品】敏感肌洗面乳", "【專科】胺基酸溫和潔顏慕斯"]},
            "step3_toner": {"reason": "經典泉水高安全比例，瞬間舒緩面部泛紅、刺痛與換季不適。", "items": ["【Avene 雅漾】舒護活泉水", "【理膚寶水】溫和舒緩噴霧", "【理膚寶水】多容安舒緩保濕化妝水"]},
            "step4_essence": {"reason": "無色素香料之極簡積雪草B5精華，給予受損屏障最基礎的安全補水。", "items": ["【Neogence 霓淨思】積雪草B5修護純粹精華", "【無印良品】敏感肌保濕精華液", "【Solone】敏感肌保濕精華"]},
            "step5_cream": {"reason": "最單純、不加重防禦負擔的開架低敏感保濕鎖水神經醯胺乳液。", "items": ["【CeraVe 適樂膚】長效清爽保濕乳", "【無印良品】敏感肌乳液", "【Cetaphil 舒特膚】長效潤膚乳"]},
            "step6_sunscreen": {"reason": "開架明星純物理防曬配方，零酒精零香料，上臉絕不刺痛發紅。", "items": ["【Curel 珂潤】潤浸保濕防曬乳", "【無印良品】敏感肌防曬乳", "【Orbis】透妍潤色隔離霜"]},
            "step7_base": {"reason": "無添加安全低敏隔離乳，溫和修正面部泛紅，不增加負擔。", "items": ["【CEZANNE】長效保濕防曬隔離乳", "【Media 媚點】保濕妝前乳", "【1028】舒敏妝前打底乳"]},
            "step8_concealer": {"reason": "通過低敏測試的開架暢銷遮瑕，安全掩蓋面部紅血絲與瑕疵，無負擔。", "items": ["【Maybelline 媚比琳】FIT ME 遮瑕膏", "【1028】服服貼貼遮瑕膏", "【heme】無瑕持久遮瑕蜜"]},
            "step9_foundation": {"reason": "經典溫和礦物成分底妝，對肌膚負擔極小，不易引發敏感突發。", "items": ["【Media 媚點】粉嫩保濕礦物粉底霜", "【INTEGRATE】柔焦輕透美肌粉餅", "【媚點】自然肌透持效粉底液"]},
            "step10_powder": {"reason": "極簡無刺激礦物蜜粉，輕盈定妝，不給脆弱皮膚帶來任何負擔。", "items": ["【CEZANNE】抗UV保濕蜜粉餅", "【neuve 惹我】清爽吸油蜜粉", "【Canmake】棉花糖蜜粉餅低敏版"]},
            "step_eyebrow": {"reason": "通過低敏測試的經典柔滑眉筆，不刮傷受損角質。", "items": ["【heme】極細持色眉筆", "【無印良品】木軸眉筆", "【1028】精算持色細眉筆"]},
            "step_contour": {"reason": "純淨無香料低刺激修容，避開泛紅區域發炎。", "items": ["【heme】三色修容餅", "【CEZANNE】小臉修容粉", "【Solone】神隱修容餅"]}
        },
        "2": { # 💎 500～1000元
            "step1_remover": {"reason": "經典醫美高效低摩擦舒敏潔膚水，溫和度與安全度萬年公認第一。", "items": ["【BIODERMA 貝德瑪】舒敏潔膚液", "【理膚寶水】高效溫和卸妝水", "【Curel 珂潤】潤浸保濕卸妝凝露"]},
            "step2_cleanser": {"reason": "超細緻綿密醫美慕斯，大幅減少雙手與脆弱肌膚的摩擦物理傷害。", "items": ["【Curel 珂潤】潤浸保濕洗顏慕斯", "【理膚寶水】多容安泡沫洗面乳", "【Dr.Wu】玻尿酸保濕潔顏慕斯"]},
            "step3_toner": {"reason": "醫美核心維生素B5化妝水，快速壓制突發泛紅與刺痛不適。", "items": ["【理膚寶水】多容安舒緩保濕化妝水", "【Dr.Wu】玻尿酸保濕精華化妝水", "【雅漾】舒敏修護保濕精華水"]},
            "step4_essence": {"reason": "萬用明星B5修護精華，強效維護脆弱物理屏障，退紅效果最直觀。", "items": ["【理膚寶水】B5舒緩保濕修護精華", "【Dr.Wu】積雪草舒敏修護精華", "【Neogence 霓淨思】積雪草B5修護純粹精華"]},
            "step5_cream": {"reason": "醫美萬用修復霜始祖，迅速壓制泛紅、粗糙脫屑與突發性刺痛。", "items": ["【理膚寶水】B5+全面修復霜", "【Curel 珂潤】潤浸保濕深層乳霜", "【雅漾】舒敏修護保濕霜"]},
            "step6_sunscreen": {"reason": "100%醫美級純物理高防禦防曬，敏弱肌全天候最安心的防護牆。", "items": ["【Avene 雅漾】全效抗UV物理防曬乳", "【理膚寶水】全護純物理亮白防曬隔離乳", "【Dr.Wu】低敏物理防曬乳"]},
            "step7_base": {"reason": "專為敏弱肌研發的低刺激明星持妝乳，長效保濕、築起物理防護牆。", "items": ["【d program 敏感話題】敏弱飾底乳", "【Curel 珂潤】潤浸保濕屏護妝前乳", "【MINON】豐潤保濕修飾防曬乳"]},
            "step8_concealer": {"reason": "護膚級抗敏低刺激遮瑕，全面隱形泛紅微血管，絕不刺激傷口。", "items": ["【d program 敏感話題】敏弱遮瑕膏", "【Medicube】修護遮瑕液", "【Nov 娜芙】低敏遮瑕膏"]},
            "step9_foundation": {"reason": "經典敏弱肌專用底妝系列，不含香料酒精，大幅降低化學負擔。", "items": ["【d program 敏感話題】敏弱蜜粉餅", "【Curel 珂潤】潤浸保濕屏護粉底液", "【Nov 娜芙】礦物粉餅"]},
            "step10_powder": {"reason": "安心舒緩醫美修護噴霧，有效取代傳統乾粉、降溫並定妝。", "items": ["【理膚寶水】多容安舒緩修護噴霧", "【Avene 雅漾】舒護活泉水", "【Curel 珂潤】潤浸保濕微粒子噴霧"]},
            "step_eyebrow": {"reason": "日本權威低敏品牌研發，滑順零拉扯，不引起眼周敏感發炎。", "items": ["【Nov 娜芙】極細柔滑眉筆", "【d program 敏感話題】敏弱立體雙頭眉筆", "【Orbis】完美持色眉筆"]},
            "step_contour": {"reason": "通過嚴格低敏測試的礦物修容，修飾臉型同時杜絕刺痛發紅。", "items": ["【Nov 娜芙】柔霧雙色修容粉", "【ETVOS】礦物修容/打亮餅", "【d program 敏感話題】敏弱頰彩修容盤"]}
        },
        "3": { # 👑 1000元以上
            "step1_remover": {"reason": "頂級草本低敏植物潔膚油，在極致安全零刺激下秒速溶解防水彩妝。", "items": ["【DARPHIN】全效舒緩卸妝乳", "【THREE】平衡潔膚油", "【植村秀】抹茶精萃潔顏油"]},
            "step2_cleanser": {"reason": "高奢極致溫和胺基酸洗顏，徹底淨化同時完美撫平脆弱肌理。", "items": ["【THREE】平衡潔膚蜜", "【SK-II】全效活膚潔面乳", "【香奈兒】深海系列潔顏慕斯"]},
            "step3_toner": {"reason": "貴婦級傳奇修護精華水，富含高奢穩定修護因子，根治脆弱敏感。", "items": ["【SK-II】青春露", "【LANCOME 蘭蔻】絕對完美玫瑰修護露", "【LA MER 海洋拉娜】濃縮精華露"]},
            "step4_essence": {"reason": "殿堂級植萃舒緩神級小粉紅，徹底阻斷物理與化學發炎刺激。", "items": ["【DARPHIN】全效舒緩精華小粉紅", "【LA MER 海洋拉娜】濃縮精華", "【蘭蔻】超未來肌因賦活露(小黑瓶)"]},
            "step5_cream": {"reason": "傳奇專櫃頂級屏障修護乳霜，提供神級修護力，讓脆弱肌原地重生。", "items": ["【海洋拉娜】經典乳霜", "【SHISEIDO 資生堂】百優精純乳霜", "【Kiehl's 契爾氏】冰河醣蛋白保濕霜"]},
            "step6_sunscreen": {"reason": "貴婦級物理抗老防曬，細緻輕盈，全面阻斷敏感泛紅惡化。", "items": ["【肌膚之鑰】全效防護乳", "【CHANEL】珍珠光感超淨化防護乳", "【DIOR】雪晶靈輕透防曬隔離乳"]},
            "step7_base": {"reason": "明星全能妝前凝霜，兼具修飾泛紅、平滑紋理與平衡面部屏障。", "items": ["【蘿拉蜜思】煥顏凝露經典型", "【肌膚之鑰】光采無瑕妝前凝霜", "【植村秀】無極限保濕妝前乳"]},
            "step8_concealer": {"reason": "高奢養膚保濕遮瑕，極致貼膚輕盈，完美隱蔽面部泛紅微血管。", "items": ["【肌膚之鑰】皆效無瑕遮瑕膏", "【NARS】奢質絲柔持妝遮瑕霜", "【LA MER 海洋拉娜】奇蹟煥采遮瑕膏"]},
            "step9_foundation": {"reason": "專利養膚精華粉底，將彩妝對敏弱肌的化學負擔降至最低、長效持妝。", "items": ["【SHISEIDO 資生堂】超進化持久粉底液", "【BOBBI BROWN】冬蟲夏草精華粉底", "【植村秀】無極限超時輕粉底"]},
            "step10_powder": {"reason": "專櫃奢華極細透明蜜粉，完美柔焦，對敏弱肌膚極致零摩擦物理負擔。", "items": ["【蘿拉蜜思】煥顏透明蜜粉", "【香奈兒】輕盈完美蜜粉", "【肌膚之鑰】光采蜜粉"]},
            "step_eyebrow": {"reason": "流暢零拉扯的殿堂級專櫃眉筆，對敏感眼周眉骨極致溫和。", "items": ["【肌膚之鑰】線條美眉筆", "【Suqqu】晶采柔飾眉筆", "【香奈兒】持久防水眉筆"]},
            "step_contour": {"reason": "高奢全天然植物系礦物修容，粉質細緻至極，完美立體五官且杜絕發炎。", "items": ["【Chantecaille 香緹卡】真實肌膚修容餅", "【Suqqu】晶采淨妍雙色修容盤", "【肌膚之鑰】立體打亮修容盤"]}
        }
    }
}

# ==============================================================================
# 🎨 2. 風格彩妝推薦資料庫
# ==============================================================================
MAKEUP_STYLE_DATABASE = {
    "1": { 
        "style_name": "✨ 韓系暖調大地色系妝容",
        "budget_data": {
            "1": {"eyeshadow": ["【1028】飛我莫屬限量眼彩盤 #杏影大地", "【heme】六色眼影盤 #大地"], "blusher": ["【Romand】勝過完美腮紅", "【heme】純色腮紅"], "lipstick": ["【Romand】果汁水光唇釉", "【1028】野熟唇釉"]},
            "2": {"eyeshadow": ["【CLIO】璀璨星沙十色眼影盤", "【3CE】九色眼影盤 #DEAR NUDE"], "blusher": ["+【3CE】單色腮紅", "【M·A·C】持色奶凍腮紅"], "lipstick": ["【3CE】絲絨霧面唇釉", "【M·A·C】子彈頭唇膏"]},
            "3": {"eyeshadow": ["【TOM FORD】高級定製四格眼盤", "【CHANEL】四色眼影盤"], "blusher": ["【NARS】炫色腮紅", "【DIOR】藍星腮紅"], "lipstick": ["【DIOR】癮誘唇膏", "【YSL】奢華緞面絨霧唇膏"]}
        }
    },
    "2": { 
        "style_name": "🌹 溫柔玫瑰粉棕色系妝容",
        "budget_data": {
            "1": {"eyeshadow": ["【heme】六色眼影盤 #玫瑰蜜桃", "【Canmake】完美高效眼影盤"], "blusher": ["【Canmake】花漾戀愛修容組", "【Romand】完美腮紅"], "lipstick": ["【Romand】果汁水光唇釉", "【CEZANNE】持久潤澤唇膏"]},
            "2": {"eyeshadow": ["【3CE】九色眼影盤 #OVERTAKE", "【CLIO】十色眼影盤 #櫻花粉"], "blusher": ["【Clinique】小雛菊腮紅", "【3CE】單色腮紅"], "lipstick": ["【M·A·C】絲柔粉霧唇釉", "【Pony Effect】奢華唇釉"]},
            "3": {"eyeshadow": ["【SUQQU】晶采盈緻眼彩盤", "【DIOR】經典五色眼影 #玫瑰色"], "blusher": ["【CHANEL】圓形腮紅", "【NARS】炫色腮紅"], "lipstick": ["【Tom Ford】設計師唇膏", "【CHANEL】COCO晶亮水唇膏"]}
        }
    },
    "3": { 
        "style_name": "🕶️ 輕歐美俐落消腫冷灰棕妝容",
        "budget_data": {
            "1": {"eyeshadow": ["【Solone】經典單色眼影自組盤", "【1028】飛我莫屬限量眼彩盤 #灰調"], "blusher": ["【heme】純色腮紅 #04", "【Solone】經典腮紅"], "lipstick": ["【into you】唇泥 #EM23", "【Solone】極潤緞光唇膏"]},
            "2": {"eyeshadow": ["【KATE】色影迷棕眼影盤", "【3CE】九色眼影盤 #SOME DEF"], "blusher": ["【3CE】單色腮紅", "【Clinique】小雛菊腮紅 #修容色"], "lipstick": ["【M·A·C】時尚唇膏 #Taupe", "【3CE】絲絨霧面唇釉"]},
            "3": {"eyeshadow": ["【DIOR】經典五色眼影 #酷灰", "【TOM FORD】四格眼盤 #消腫灰"], "blusher": ["【NARS】霧光修容餅", "【CHANEL】圓形腮紅"], "lipstick": ["【YSL】小黑條口紅 #314", "【DIOR】藍星唇膏"]}
        }
    },
    "4": { 
        "style_name": "🥛 白開水偽素顏輕透妝容",
        "budget_data": {
            "1": {"eyeshadow": ["【Canmake】完美霧面眉影盤", "【heme】六色眼影盤 #純淨"], "blusher": ["【heme】純色腮紅 #10", "【CEZANNE】單色腮紅"], "lipstick": ["【CEZANNE】持久潤澤唇膏", "【OPERA】金管唇膏"]},
            "2": {"eyeshadow": ["【Excel】裸色深邃眼影盤 #SR01", "【KATE】色影迷棕眼影盤"], "blusher": ["【Clinique】小雛菊腮紅 #18", "【3CE】柔霧腮紅"], "lipstick": ["【OPERA】柔潤唇膏", "【M·A·C】子彈頭護唇膏"]},
            "3": {"eyeshadow": ["【BOBBI BROWN】時尚奢華眼影", "【SUQQU】晶采盈緻眼彩盤"], "blusher": ["【SUQQU】晶采淨妍頰彩", "【DIOR】藍星腮紅"], "lipstick": ["【CHANEL】COCO晶亮水唇膏", "【DIOR】豐漾俏唇蜜"]}
        }
    },
    "5": { 
        "style_name": "⏰ 早八快速妝容",
        "budget_data": {
            "1": {"eyeshadow": ["【Solone】單色霧面消腫眼影", "【Canmake】雙色快捷眼影"], "blusher": ["【heme】純色腮紅 #10", "【惹我】清爽腮紅"], "lipstick": ["【OPERA】柔潤唇膏", "【CEZANNE】持久潤澤唇膏"]},
            "2": {"eyeshadow": ["【KATE】雙色亮片眼影盤", "【1028】飛我莫屬限量眼彩盤"], "blusher": ["【M·A·C】持色奶凍腮紅", "【3CE】液態腮紅"], "lipstick": ["【I'M MEME】我愛心機水光唇萃", "【Romand】果汁水光唇釉"]},
            "3": {"eyeshadow": ["【BOBBI BROWN】流雲持久防水眼影筆", "【LAURA MERCIER】夢露煙燻眼影筆"], "blusher": ["【NARS】多功能彩妝膏", "【CHANEL】泡泡腮紅"], "lipstick": ["【DIOR】癮誘粉漾潤唇膏", "【CHANEL】COCO晶亮水唇膏"]}
        }
    }
}

TUTORIAL_DATABASE = {
    "skincare_by_type": {
        "oil": {"title": "Dr. Ivan 6 - 混合肌與油肌分區控油穩膚防脫皮教學", "url": "https://www.youtube.com/results?search_query=Dr+Ivan+6+%E6%B7%B7%E5%90%88%E8%82%8C+%E4%BF%9D%E9%A4%8A"},
        "mix": {"title": "Dr. Ivan 6 - 混合肌與油肌分區控油穩膚防脫皮教學", "url": "https://www.youtube.com/results?search_query=Dr+Ivan+6+%E6%B7%B7%E5%90%88%E8%82%8C+%E4%BF%9D%E9%A4%8A"},
        "dry": {"title": "Dr. Ivan 6 - 乾燥肌缺水密集補水防脫屑起皮教學", "url": "https://www.youtube.com/results?search_query=Dr+Ivan+6+%E4%B9%BE%E6%80%A7%E8%82%8C+%E4%BF%9D%E9%A4%8A"},
        "sensitive": {"title": "皮膚科醫生 - 敏感肌與泛紅肌極簡退紅屏障修護學理", "url": "https://www.youtube.com/results?search_query=%E6%95%8F%E6%84%9F%E8%82%8C+%E4%BF%9D%E9%A4%8A+%E9%86%AB%E7%94%9F"}
    },
    "skincare_basic": {"title": "皮膚科莊盈彥醫師 - 基礎護膚學理與正確保養順序", "url": "https://www.youtube.com/results?search_query=%E8%8E%8A%E7%9B%88%E5%BD%A5+%E4%BF%9D%E9%A4%8A%E9%A0%86%E5%BA%8F"},
    "makeup_styles": {
        "1": {"title": "PONY - 韓系日常大地色消腫暖調妝容完整教學", "url": "https://www.youtube.com/results?search_query=PONY+%E9%9F%93%E7%B3%BB%E5%A4%A7%E5%9C%B0%E8%89%B2%E5%A6%9D%E5%AE%B9"},
        "2": {"title": "一枝南南 - 溫柔玫瑰粉棕色大面積腮紅招桃花約會妝", "url": "https://www.youtube.com/results?search_query=%E4%B8%80%E6%9E%9D%E5%8D%97%E5%8D%97+%E7%8E%AB%E7%91%B0%E7%B2%89%E6%A3%95%E5%A6%9D%E5%AE%B9"},
        "3": {"title": "Jcnana 蒨蒨 - 亞洲面孔消腫冷灰棕妝容與輕歐美結構修容術", "url": "https://www.youtube.com/results?search_query=Jcnana+%E5%86%B7%E7%11%B0%E6%A3%95%E5%A6%9D%E5%AE%B9"},
        "4": {"title": "鴨鴨 Makeup - 低粉感、低飽和無心機『白開水純欲妝』核心教學", "url": "https://www.youtube.com/results?search_query=%E9%B4%A8%E9%B4%A8+Makeup+%E5%85%AA%E9%96%8B%E6%B0%B4%E5%A6%9D%E5%AE%B9"},
        "5": {"title": "早八快速完妝教學 - 5分鐘俐落出門防遲到快速彩妝術", "url": "https://www.youtube.com/results?search_query=%E6%97%A9%E5%85%AB+%E5%BF%AB%E9%80%9F%E5%A6%9D%E5%AE%B9"}
    }
}

# ==============================================================================
# 🛠️ 輔助功能：精準動態跳轉連結生成器
# ==============================================================================
def render_search_link(brand_and_product):
    clean_name = brand_and_product.replace("【", "").replace("】", " ").split("#")[0].strip()
    encoded_name = urllib.parse.quote(clean_name)
    
    google_shopping_url = f"https://www.google.com/search?tbm=shop&q={encoded_name}"
    dcard_url = f"https://www.google.com/search?q={urllib.parse.quote(clean_name + ' 心得 site:dcard.tw')}"
    
    col1, col2 = st.columns(2)
    with col1: st.markdown(f"🛍️ [🛒 查最新在售通路與真實即時價格]({google_shopping_url})")
    with col2: st.markdown(f"💬 [🔍 點我查 Dcard 網友長青回購心得]({dcard_url})")

# ==============================================================================
# 3. Streamlit 網頁介面與狀態鎖定設計 (💡 核心錯誤修正點)
# ==============================================================================
st.set_page_config(page_title="專業級智能美妝護膚諮詢系統", page_icon="💄", layout="centered")

# ⚡ 初始化 Session State：如果沒有點過生成報告，預設狀態是 False
if "generate_report" not in st.session_state:
    st.session_state.generate_report = False

st.title("💄 專業級智能美妝與護膚諮詢系統")
st.write("精準分析：提供『日間妝前保養、完美底妝、風格彩妝』一站式客製化學理護膚指南。")
st.markdown("---")

st.header("🔍 請輸入您的個人條件")

mode_option = st.radio(
    "💡 請選擇系統運作模式：",
    ["🌞 13步精緻全妝指南 (日間保養+底妝+彩妝)", "🌙 5步深夜保養修護 (夜間清潔+深度鎖水)"],
    index=0
)
is_night_mode = "5步深夜保養修護" in mode_option

skin_options = {"油性肌/痘痘肌": "oil", "乾燥肌/缺水肌": "dry", "混合肌": "mix", "敏感肌/泛紅肌": "sensitive"}
user_skin_label = st.selectbox("1. 您的主要膚質是什麼？", list(skin_options.keys()))
user_skin = skin_options[user_skin_label]

budget_options = {"💰 500元以下產品 (低預算)": "1", "💎 500～1000元產品 (中預算)": "2", "👑 1000元以上產品 (高預算)": "3"}
user_budget_label = st.selectbox("2. 您的產品價格帶？", list(budget_options.keys()))
user_budget = budget_options[user_budget_label]

style_label_options = list(MAKEUP_STYLE_DATABASE.keys())
user_style_label = st.selectbox(
    "3. 您今天想搭配哪一種彩妝風格？", 
    [MAKEUP_STYLE_DATABASE[k]["style_name"] for k in style_label_options], 
    disabled=is_night_mode,
    help="當切換為『深夜保養修護』模式時，此選單會自動禁用。"
)

user_style = "1"
for k, v in MAKEUP_STYLE_DATABASE.items():
    if v["style_name"] == user_style_label:
        user_style = k

btn_text = "🚀 生成夜間深度保養修護報告" if is_night_mode else "🚀 生成客製化 13 步美妝護膚報告"

# ⚡ 當按下按鈕時，將狀態設為 True
if st.button(btn_text, use_container_width=True):
    st.session_state.generate_report = True

# ⚡ 只要 generate_report 是 True，不管頁面怎麼重跑（選取商品），內容都絕對不會消失！
if st.session_state.generate_report:
    st.markdown("---")
    
    skin_info = SKIN_DATABASE[user_skin]
    skin_dict = skin_info[user_budget]
    
    if is_night_mode:
        # ==========================================================================
        # 🌙 模式 A：深夜保養修護報告 (5 步驟)
        # ==========================================================================
        st.header(f"🎉 您的深夜保養修護報告")
        st.info(skin_info["diagnosis"])
        
        st.subheader("🧴 核心修護階段：深夜保養 (STEP 1 ~ 5)")
        night_steps = [
            ("STEP 1【深層卸妝步驟】", "step1_remover"),
            ("STEP 2【溫和潔顏步驟】", "step2_cleanser"),
            ("STEP 3【二次調理化妝水】", "step3_toner"),
            ("STEP 4【高濃度密集精華修護】", "step4_essence"),
            ("STEP 5【最後鎖水厚敷乳霜】", "step5_cream")
        ]
        for step_title, db_key in night_steps:
            with st.expander(step_title, expanded=True):
                st.markdown(f"💡 **夜間學理修護理由**：{skin_dict[db_key]['reason']}")
                st.markdown("**📋 推薦的精選品項：**")
                
                selected_item = st.radio(f"挑選一個適合妳的經典產品：", skin_dict[db_key]['items'], key=f"night_{db_key}")
                render_search_link(selected_item)
    else:
        # ==========================================================================
        # 🌞 模式 B：精緻全妝指南 (13 步驟)
        # ==========================================================================
        st.header(f"🎉 您的 13 步客製化報告")
        st.write(f"🎨 **當前搭配風格**：{user_style_label} | 預算價格帶：{user_budget_label}")
        st.info(skin_info["diagnosis"])
        
        style_info = MAKEUP_STYLE_DATABASE[user_style]
        raw_makeup_lists = style_info["budget_data"][user_budget]
        
        # 🧴 PART 1：日間妝前保養與完美底妝 (STEP 1 ~ 10)
        st.subheader("🧴 第一階段：日間極致妝前與底妝 (STEP 1 ~ 10)")
        day_steps = [
            ("STEP 1【妝前基礎補水：化妝水步驟】", "step3_toner"),
            ("STEP 2【妝前深層保濕：精華液步驟】", "step4_essence"),
            ("STEP 3【妝前輕盈鎖水：乳霜/凝凍步驟】", "step5_cream"),
            ("STEP 4【日間高效防禦：防曬乳步驟】", "step6_sunscreen"),
            ("STEP 5【底妝校色打底：飾底乳步驟】", "step7_base"),
            ("STEP 6【局部瑕疵隱形：重點遮瑕步驟】", "step8_concealer"),
            ("STEP 7【全臉完美無瑕：粉底液上妝】", "step9_foundation"),
            ("STEP 8【全天鎖水控油：蜜粉定妝步驟】", "step10_powder"),
            ("STEP 9【精神元氣加分：完美眉彩步驟】", "step_eyebrow"),
            ("STEP 10【立體五官輪廓：修容高光步驟】", "step_contour")
        ]
        
        for step_title, db_key in day_steps:
            with st.expander(step_title, expanded=True):
                st.markdown(f"💡 **日間學理推薦理由**：{skin_dict[db_key]['reason']}")
                st.markdown("**📋 推薦的精選品項：**")
                
                selected_item = st.radio(f"挑選一個最直觀適合妳的產品：", skin_dict[db_key]['items'], key=f"day_{db_key}")
                render_search_link(selected_item)
                
        # 🎨 PART 2：風格彩妝階段 (STEP 11 ~ 13)
        st.markdown("---")
        st.subheader(f"🎨 第二階段：{style_info['style_name']} 精緻彩妝 (STEP 11 ~ 13)")
        
        style_steps = [
            ("STEP 11【靈魂亮點：客製化風格眼影盤】", "eyeshadow"),
            ("STEP 12【氛圍元氣：命定高氣色腮紅】", "blusher"),
            ("STEP 13【點睛之筆：完美質地完美唇彩】", "lipstick")
        ]
        
        for step_title, makeup_key in style_steps:
            with st.expander(step_title, expanded=True):
                st.markdown("**📋 精選風格品項：**")
                selected_item = st.radio(f"選擇一個查看即時比價：", raw_makeup_lists[makeup_key], key=f"style_{makeup_key}")
                render_search_link(selected_item)

    # ==============================================================================
    # 📺 共通區塊：影音教程推薦
    # ==============================================================================
    st.markdown("---")
    st.subheader("📺 專屬線上影音教程推薦")
    st.link_button(f"🧴 {TUTORIAL_DATABASE['skincare_basic']['title']}", TUTORIAL_DATABASE['skincare_basic']['url'])
    
    specific_skincare = TUTORIAL_DATABASE["skincare_by_type"][user_skin]
    st.link_button(f"🧴 {specific_skincare['title']}", specific_skincare['url'])
    
    if not is_night_mode:
        specific_makeup = TUTORIAL_DATABASE["makeup_styles"][user_style]
        st.link_button(f"🎨 {specific_makeup['title']}", specific_makeup['url'])