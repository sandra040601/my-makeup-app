import streamlit as st

# ==============================================================================
# 🗂️ 1. 膚質保養與底妝資料庫 (含有完整 10 個步驟的對應產品)
# ==============================================================================
SKIN_DATABASE = {
    "oil": {
        "diagnosis": "【油性肌/痘痘肌學理診斷】\n臨床特徵為皮脂腺分泌過度旺盛。💡 產品挑選關鍵：應優先選擇含有『控油成分』或『酸類代謝成分』之清爽產品，避免毛孔阻塞。",
        "1": {
            "step1_remover": {"reason": "清爽水狀質地，溫和溶解油脂且不易致痘致粉刺。", "items": ["【妮維雅】雙層極淨卸妝水 $259", "【1028】深層潔淨卸妝水 $199", "【Biore】高效 active 卸妝水 $210"]},
            "step2_cleanser": {"reason": "微米控油泡沫，能深入毛孔洗淨多餘皮脂與髒污。", "items": ["【專科】超微米控油潔顏乳 $135", "【曼秀雷敦】Acnes抗痘洗面乳 $125", "【Biore】抗痘保濕洗面乳 $110"]},
            "step3_toner": {"reason": "二次清潔並調理角質，給予最基礎的清爽補水與收斂。", "items": ["【Imju】薏仁清潤化妝水 $199", "【自白肌】特濃玻尿酸保濕化妝水 $290", "【專科】保濕專科化妝水 $260"]},
            "step4_essence": {"reason": "極輕透的水感補水精華，避開黏膩感並強效控油。", "items": ["【Solone】補水控油噴霧精華 $119", "【L'Oreal】青春密碼酵素肌底精華 $399", "【Neogence】玻尿酸保濕精華液 $450"]},
            "step5_cream": {"reason": "凝凍狀鎖水無負擔，補水不補油，徹底杜絕悶痘。", "items": ["【雪芙蘭】水潤凝霜 $129", "【Curel】控油保濕水凝露 $420", "【肌研】極潤保濕水凝凍 $380"]},
            "step6_sunscreen": {"reason": "超清爽無油防曬配方，成膜快速、不致粉刺、不泛油光。", "items": ["【Maybelline】反孔特霧防曬乳 $350", "【1028】超控油防曬隔離乳 $290", "【曼秀雷敦】水潤肌超保濕水感防曬露 $379"]},
            "step7_base": {"reason": "強力吸附油脂，延緩全臉暗沉並修正粗大毛孔。", "items": ["【1028】超控油饰底乳 $299", "【SOFINA】漾緁控油瓷效妝前乳 $350", "【媚點】零瑕美肌妝前乳 $220"]},
            "step8_concealer": {"reason": "高遮瑕且質地偏乾的霧面遮瑕，完美鎖死痘疤與局部泛紅。", "items": ["【1028】服服貼貼遮瑕膏 $280", "【heme】無瑕持久遮瑕蜜 $300", "【Maybelline】FIT ME遮瑕膏 $300"]},
            "step9_foundation": {"reason": "微米控油科技或高遮瑕霧面粉體，打造長效啞光妝感。", "items": ["【Maybelline】反孔特霧粉底液 $420", "【1028】極上鏡柔光超磁控粉底液 $390", "【KATE】零瑕肌密微霧粉底液 $540"]},
            "step10_powder": {"reason": "極佳的乾粉吸油力，強力鎖死面部油脂並極致柔焦。", "items": ["【惹我】清爽吸油蜜粉 $145", "【innisfree】無油無慮礦物控油蜜粉 $250", "【1028】超吸油蜜粉餅 $159"]}
        },
        "2": {
            "step1_remover": {"reason": "醫美級平衡皮脂分泌配方，溫和卸妝不破壞皮脂膜。", "items": ["【貝德瑪】平衡控油潔膚液 $450", "【理膚寶水】高效溫和卸妝水 $480", "【雅漾】控油清爽潔膚水 $500"]},
            "step2_cleanser": {"reason": "胺基酸溫和洗淨配方，調理皮脂同時保護肌膚屏障。", "items": ["【Curel】控油保濕洗顏慕斯 $400", "【Dr.Wu】適肌控油潔顏慕斯 $420", "【理膚寶水】深層控油泡沫洗面乳 $480"]},
            "step3_toner": {"reason": "清爽控油化妝水，軟化角質並溫和收斂毛孔。", "items": ["【Origin】品木宣言靈芝水 $520", "【Kiehl's】金盞花植物精華化妝水 $750", "【Labo Labo】毛孔緊緻化妝水 $420"]},
            "step4_essence": {"reason": "含有水楊酸精華，代謝老廢角質並深度淨化毛孔。", "items": ["【寶拉珍選】2%水楊酸精華液 $520", "【Dr.Wu】杏仁酸亮白煥膚精華 $600", "【理膚寶水】淨痘無瑕極效精華 DUO+ $950"]},
            "step5_cream": {"reason": "清爽控油乳液，有效抑制全天候的過度皮脂分泌。", "items": ["【理膚寶水】毛孔緊緻控油保濕乳 $790", "【Vichy】新皮脂平衡多效精華乳 $850", "【雅漾】控油清爽保濕乳 $780"]},
            "step6_sunscreen": {"reason": "醫美級抗油全效防曬，清爽不黏膩且不誘發痘痘發炎。", "items": ["【理膚寶水】全護清爽防曬液 $800", "【雅漾】控油清爽防曬乳 $850", "【Dr.Wu】全效控油防曬乳 $720"]},
            "step7_base": {"reason": "兼具長效持妝與抗暗沉效果的柔焦打底妝前乳。", "items": ["【Pony Effect】水透光控油妝前乳 $690", "【MAQuillAGE】心機星魅平衡持妝控油乳 $720", "【Espoir】純素控油妝前乳 $650"]},
            "step8_concealer": {"reason": "抗油抗汗的高持久度遮瑕，不易位移變色、完美隱形痘痘。", "items": ["【CLIO】無瑕持妝遮瑕膏 $450", "【J/X】三色遮瑕膏 $580", "【The Saem】完美遮瑕液 $350"]},
            "step9_foundation": {"reason": "中高價位抗油抗汗防裂粉底，霧面妝效持久不浮粉。", "items": ["【KATE】零瑕肌密持緞粉底液 $540", "【CLIO】柔霧光澤持妝粉底液 $680", "【Pony Effect】絕對遮瑕隱形粉底液 $790"]},
            "step10_powder": {"reason": "超強效定妝控油，全天候維持高級微霧面妝感。", "items": ["【Pony Effect】絕對持久定妝噴霧 $550", "【I'M MEME】我愛油光除霧蜜粉餅 $290", "【banila co】空氣感控油蜜粉 $450"]}
        },
        "3": {
            "step1_remover": {"reason": "專櫃頂級潔顏油，深入毛孔徹底溶解黑頭與頑固彩妝。", "items": ["【植村秀】黑米精萃潔顏油 $1200", "【BOBBI BROWN】沁透茉莉淨妝油 $1350", "【CLINIQUE】溫和卸妝膏 $1150"]},
            "step2_cleanser": {"reason": "頂級絲滑泡沫，深層淨化毛孔同時維持肌膚細緻膚感。", "items": ["【SK-II】全效活膚潔面乳 $1500", "【香奈兒】深海系列潔顏慕斯 $1650", "【DIOR】雪晶靈透亮潔顏乳 $1450"]},
            "step3_toner": {"reason": "高奢調理精華水，平衡油脂並全面提升肌膚透亮度。", "items": ["【SK-II】青春露 $3500", "【ESTEE LAUDER】微分子肌底原生露 $2200", "【LANCOME】超極光活粹晶露 $2500"]},
            "step4_essence": {"reason": "頂級修護與控油精華，調理粗大毛孔、瑕疵不留痕跡。", "items": ["【修麗可】果酸全面調理精華 $1800", "【CLARINS】超級精華黃金雙激萃 $2200", "【Aesop】輕盈保濕精華露 $1650"]},
            "step5_cream": {"reason": "極致清爽零油光水凝凍，24小時封閉保濕卻膚感輕盈。", "items": ["【Kiehl's】冰河醣蛋白吸油水凝凍 $1600", "【CLINIQUE】水磁場100H活水循環凝膠 $1500", "【BIOTHERM】極量控油水凝凍 $1400"]},
            "step6_sunscreen": {"reason": "專櫃頂級抗老防曬，水感不油悶、完美阻絕紫外線老損。", "items": ["【肌膚之鑰】無瑕防曬護膚膏 $2500", "【LANCOME】超輕盈UV水凝露 $1950", "【SHISEIDO】防曬無油防護乳 $1500"]},
            "step7_base": {"reason": "專櫃級水感控油打底，平滑毛孔、神級持妝對抗中東油田。", "items": ["【YSL】名模肌密光燦水凝露 $2150", "【M·A·C】超顯白持妝乳 $1450", "【GIVENCHY】高級訂製妝前打底乳 $1600"]},
            "step8_concealer": {"reason": "奢華絲滑高粉體遮瑕，不乾不裂、一抹完美霧化痘痘暗沉。", "items": ["【NARS】奢華絲柔持妝遮瑕霜 $1100", "【肌膚之鑰】皆效無瑕遮瑕膏 $2000", "【DIOR】超完美持久遮瑕乳 $1300"]},
            "step9_foundation": {"reason": "油肌終極專櫃救星，越夜越美麗，抗油抗汗不脫妝。", "items": ["【雅詩蘭黛】粉持久完美持妝粉底 $2100", "【植村秀】無極限超時輕粉底 $1900", "【YSL】恆久完美無瑕持妝粉底 $2300"]},
            "step10_powder": {"reason": "煙霧般頂級細緻粉體，徹底鎖死油光並全面柔焦毛孔。", "items": ["【M·A·C】超持妝輕透鏡蜜粉 $1500", "【LAURA MERCIER】煥顏透明蜜粉 $1500", "【GIVENCHY】高級訂製四格蜜粉 $2200"]}
        }
    },
    "dry": {
        "diagnosis": "【乾燥肌/缺水肌學理診斷】\n臨床特膚為角質層含水量屏障受損。💡 產品挑選關鍵：必須優先選擇含有『高保濕因子』或『親膚性植物油』的潤澤型產品，避免乾裂卡粉。",
        "1": {
            "step1_remover": {"reason": "乳狀質地減少對乾肌的摩擦，溫和卸妝且不帶走天然油脂。", "items": ["【Biore】深層卸妝乳 $179", "【Pond's】旁氏冷霜卸妝膏 $160", "【妮維雅】保濕深層卸妝乳 $185"]},
            "step2_cleanser": {"reason": "添加玻尿酸保濕成分，洗後肌膚水嫩、完全不緊繃乾澀。", "items": ["【肌研】極潤保濕洗面乳 $240", "【專科】超微米保濕潔顏乳 $135", "【雪芙蘭】胺基酸保濕洗面乳 $120"]},
            "step3_toner": {"reason": "多重分子玻尿酸強效補水，高滲透力瞬間滋潤乾燥角質。", "items": ["【肌研】極潤保濕化妝水 $440", "【Avene】雅漾舒護活泉水 $199", "【MINON】豐潤保濕化妝水 $450"]},
            "step4_essence": {"reason": "基礎小資界高親膚保濕精華，密集深度補水修護乾紋。", "items": ["【L'Oreal】玻尿酸瞬效保濕精華 $399", "【Neogence】玻尿酸保濕精華液 $450", "【Solone】密集補水精華液 $150"]},
            "step5_cream": {"reason": "豐富封閉性油脂成分，在表皮形成嚴密鎖水防乾裂厚薄膜。", "items": ["【雪芙蘭】滋養霜 經典保濕 $79", "【NIVEA】妮維雅霜(藍罐) $120", "【CeraVe】修護保濕乳 $399"]},
            "step6_sunscreen": {"reason": "精華液質地保曬，防曬同時兼顧全天候肌膚水潤感。", "items": ["【Canmake】美人魚防曬啫喱 $300", "【雪芙蘭】超水感保濕防曬凝乳 $210", "【專科】完美防曬水凝乳 $340"]},
            "step7_base": {"reason": "高比例美容液成分打底，為乾燥肌底注入水分防止乾裂。", "items": ["【CEZANNE】長效保濕妝前乳 $290", "【Media】保濕礦物妝前乳 $220", "【SOFINA】漾緁水潤瓷效妝前乳 $350"]},
            "step8_concealer": {"reason": "添加保濕因子的水潤遮瑕液，修飾黑眼圈不卡紋、不結塊。", "items": ["【Maybelline】FIT ME遮瑕膏 $300", "【1028】服服貼貼遮瑕膏 $280", "【The Saem】重點遮瑕液 $200"]},
            "step9_foundation": {"reason": "高滋潤霜狀或乳狀質地，能完美服貼脫屑肌膚，撫平乾紋。", "items": ["【Media】粉嫩保濕礦物粉底霜 $280", "【INTEGRATE】迷人光采粉底精華 $380", "【Kate】柔焦瑕力粉底液 $450"]},
            "step10_powder": {"reason": "保濕型定妝噴霧代替乾粉，定妝同時牢牢鎖住水分。", "items": ["【1028】空氣定妝噴霧(保濕型) $350", "【防曬專科】保濕定妝噴霧 $280", "【Carome】持久保濕噴霧 $420"]}
        },
        "2": {
            "step1_remover": {"reason": "醫美級滋潤卸妝凝露，守護肌膚關鍵神經醯胺成分。", "items": ["【Curel】潤浸保濕卸妝凝露 $400", "【舒特膚】溫和卸妝乳 $450", "【理膚寶水】溫和保濕卸妝乳 $480"]},
            "step2_cleanser": {"reason": "不含皂鹼、不緊繃，專為乾性敏弱肌設計的溫和洗顏慕斯。", "items": ["【Cetaphil】溫和潔膚乳 $450", "【Curel】潤浸保濕洗顏慕斯 $480", "【理膚寶水】玻尿酸保濕洗面乳 $450"]},
            "step3_toner": {"reason": "添加神經醯胺等屏障修護成分，強效抓水的高保濕化妝水。", "items": ["【Curel】潤浸保濕化妝水 $520", "【Dr.Wu】玻尿酸保濕精華化妝水 $500", "【TUNEMAKERS】神經醯胺前導保濕水 $580"]},
            "step4_essence": {"reason": "經典修護補水精華，密集深度補水、穩定乾涸角質層。", "items": ["【雅詩蘭黛】特潤超導修護露小棕瓶(小容量) $680", "【理膚寶水】B5彈潤修復精華 $950", "【Dr.Wu】玻尿酸保濕精華液 $850"]},
            "step5_cream": {"reason": "深層修護型乳霜，有效緩解肌膚因乾燥引起的脫屑與緊繃。", "items": ["【Curel】潤浸保濕深層乳霜 $720", "【CeraVe】長效潤澤修護霜 $550", "【理膚寶水】多容安極效舒緩修護乳 $850"]},
            "step6_sunscreen": {"reason": "高滋潤物理防曬，全面折射紫外線且滋潤乾燥表皮。", "items": ["【理膚寶水】全護長效保濕防曬乳 $850", "【Curel】潤浸保濕防曬乳 $600", "【Dr.Wu】全效保濕防曬乳 $720"]},
            "step7_base": {"reason": "爆水級妝前打底乳，提供極高保濕度，維持全天底妝水潤。", "items": ["【Pony Effect】水透光妝前防護乳 $690", "【Excel】柔采光透妝前乳 $610", "【KATE】零瑕肌密濾鏡妝前乳 $390"]},
            "step8_concealer": {"reason": "高延展性保濕修護遮瑕膏，絕不乾裂卡粉、完美遮蓋瑕疵。", "items": ["【Medicube】修護遮瑕液 $480", "【d program】敏感話題敏弱遮瑕膏 $600", "【CLIO】無瑕水潤遮瑕蜜 $450"]},
            "step9_foundation": {"reason": "兼具高潤澤感與精緻透亮奶油光的保濕型粉底液。", "items": ["【CLIO】柔霧光澤水感粉底液 $680", "【Maybelline】水凝BB純淨透亮粉底膏 $450", "微【1028】極上鏡柔光超磁控粉底液(滋潤版) $390"]},
            "step10_powder": {"reason": "以高細緻微霧定妝噴霧代替乾粉定妝，緊鎖水分防止起皮。", "items": ["【Pony Effect】絕對持久定妝噴霧 $550", "【高絲】高絲美顏定妝噴霧 $360", "【SOFINA】漾緁控油定妝噴霧 $380"]}
        },
        "3": {
            "step1_remover": {"reason": "貴婦級養膚型卸妝霜，膏體化為親膚油脂，帶來頂級滋潤感。", "items": ["【EVE LOM】全能深層潔淨霜 $2500", "【DARPHIN】花梨木按摩潔面膏 $1700", "【芭比波朗】大橘子卸妝膏 $1450"]},
            "step2_cleanser": {"reason": "富含高級植物精萃與滋養成分，泡沫絲滑，洗後膚感柔嫩。", "items": ["【香奈兒】深海系列潔顏慕斯 $1650", "【肌膚之鑰】精萃光采潔膚皂 $1800", "【SUQQU】絕緻晶艷潤膚潔面乳 $1900"]},
            "step3_toner": {"reason": "高奢精華水，質地濃郁高滲透，為極度乾燥肌提供瞬時奢華滋養。", "items": ["【LANCOME】絕對完美玫瑰修護露 $2800", "【LA MER】濃縮精華露 $3500", "【SHISEIDO】紅色活酵超導奇蹟露 $2200"]},
            "step4_essence": {"reason": "專櫃頂級修護抗老精華，強效穩健屏障，告別粗糙與乾燥。", "items": ["【蘭蔻】超未來肌因賦活露小黑瓶 $3100", "【雅詩蘭黛】特潤超導修護露小棕瓶 $3200", "【香奈兒】山茶花保濕微導入精華液 $2900"]},
            "step5_cream": {"reason": "傳奇頂級修護封閉鎖水乳霜，深度滋養，徹底封死水分流失。", "items": ["【海洋拉娜】經典乳霜 $6800", "【百優】精純乳霜 $2300", "【Kiehl's】冰河醣蛋白保濕霜 $1600"]},
            "step6_sunscreen": {"reason": "奢華保養級全效防曬，極高含水量，打造極致尊榮上妝底層。", "items": ["【肌膚之鑰】全效防護乳 $3300", "【CHANEL】珍珠光感超淨化防護乳 $2000", "【DIOR】雪晶靈輕透防曬隔離乳 $2200"]},
            "step7_base": {"reason": "專櫃乾肌打底神物，瞬間撫平乾燥紋理，煥發精緻貴婦光澤。", "items": ["【蘿拉蜜思】煥顏凝露(保濕型) $1500", "【PAUL & JOE】糖瓷絲潤隔離乳 $1200", "【肌膚之鑰】光采無瑕妝前凝霜 $2100"]},
            "step8_concealer": {"reason": "貴婦級精華液基底遮瑕，極致貼膚滑順，完全隱形眼周乾紋。", "items": ["【肌膚之鑰】皆效無瑕遮瑕膏 $2000", "【BOBBI BROWN】冬蟲夏草奢華遮瑕膏 $1400", "【LA MER】奇蹟煥采遮瑕膏 $2500"]},
            "step9_foundation": {"reason": "頂級養膚精華粉底，注入滿滿精華成分，打造精緻水光肌。", "items": ["【BOBBI BROWN】冬蟲夏草精華粉底 $2600", "【LANCOME】絕對完美粉底精粹 $3200", "【SUQQU】絕緻艷澤粉霜 $380"]},
            "step10_powder": {"reason": "頂級微細乾粉，完全不乾澀、不奪走肌膚水分的奢華定妝。", "items": ["【香奈兒】輕盈完美蜜粉 $2150", "【肌膚之鑰】光采蜜粉 $2450", "【SUQQU】晶采透霧蜜粉 $2300"]}
        }
    },
    "mix": {
        "diagnosis": "【混合肌學理診斷】\n面部皮脂腺分布不均，T字部位出油旺盛而雙頰乾燥緊繃。💡 產品挑選關鍵：應選擇具有『水油平衡調節』能力或採取『分區保養底妝』策略。",
        "1": {
            "step1_remover": {"reason": "溫和且清爽平衡全臉不同區域油脂狀態的卸妝乳/水。", "items": ["【Biore】溫和卸妝乳 $179", "【妮維雅】零油感保濕卸妝水 $220", "【貝德瑪】舒敏潔膚液小資版 $300"]},
            "step2_cleanser": {"reason": "保濕成分留於雙頰，同時帶走 T 字部位皮脂的平衡潔顏乳。", "items": ["【Biore】溫和水嫩洗面乳 $115", "【專科】保濕控油洗面乳 $135", "【雪芙蘭】水肌精保濕洗面乳 $110"]},
            "step3_toner": {"reason": "純補水化妝水，既不讓 T 字黏悶，又能適度滋潤雙頰。", "items": ["【肌研】極潤保濕化妝水 $440", "【Imju】薏仁清潤化妝水 $199", "【獨島】1025獨島化妝水 $280"]},
            "step4_essence": {"reason": "質地極度輕盈的純補水型精華液，讓全臉毫無黏膩負擔。", "items": ["【Neogence】玻尿酸保濕精華液 $450", "【L'Oreal】玻尿酸瞬效保濕精華 $399", "【Solone】玻尿酸保濕精華 $150"]},
            "step5_cream": {"reason": "輕盈水凝霜質地，給予雙頰足夠鎖水力又不易悶長 T 字粉刺。", "items": ["【雪芙蘭】水潤凝霜 $129", "【Neutrogena】露得清露得清水活保濕凝露 $399", "【CeraVe】全效超級保濕乳 $450"]},
            "step6_sunscreen": {"reason": "無油水感防曬，全臉推勻快速成膜，不悶不乾、完美平衡。", "items": ["【曼秀雷敦】水潤肌超保濕水感防曬露 $379", "【妮維雅】三重防護輕感防曬凝乳 $420", "【Biore】含水防曬清透水凝露 $300"]},
            "step7_base": {"reason": "適合局部塗抹在易出油的 T 字部位，達到完美分區控油打底。", "items": ["【SOFINA】漾緁控油瓷效妝前乳 $350", "【1028】超控油飾底乳 $299", "【媚點】防曬妝前乳 $220"]},
            "step8_concealer": {"reason": "高延展度中度遮瑕蜜，完美過渡出油區與乾燥區的色差毛孔。", "items": ["【Maybelline】FIT ME遮瑕膏 $300", "【1028】服服貼貼遮瑕膏 $280", "【heme】無瑕持久遮瑕蜜 $300"]},
            "step9_foundation": {"reason": "水潤好推、不卡乾紋，對雙頰友善且兼具基本 T 字抗汗力。", "items": ["【Media】自然肌透持效粉底液 $330", "【Maybelline】反孔特霧粉底液 $420", "【INTEGRATE】柔焦輕透美肌粉底液 $380"]},
            "step10_powder": {"reason": "分區定妝，重點按壓 T 字吸附油脂，雙頰輕輕帶過。", "items": ["【1028】超吸油蜜粉餅 $159", "【惹我】清爽吸油蜜粉 $145", "【innisfree】無油無慮礦物控油蜜粉 $250"]}
        },
        "2": {
            "step1_remover": {"reason": "溫和、高清潔力且質地清爽的潔膚水，完全不留全臉黏膩感。", "items": ["【貝德瑪】舒敏潔膚液 $450", "【理膚寶水】高效溫和卸妝水 $480", "【雅漾】舒敏卸妝潔膚水 $500"]},
            "step2_cleanser": {"reason": "溫和水油平衡慕斯，洗後雙頰潤澤、T字控油清爽。", "items": ["【Dr.Wu】玻尿酸保濕潔顏慕斯 $400", "【Curel】潤浸保濕洗顏慕斯 $480", "【Cetaphil】溫和舒敏洗顏慕斯 $450"]},
            "step3_toner": {"reason": "穩定混合肌水油失衡與粗糙膚況的專門機能性化妝水。", "items": ["【Origin】品木宣言靈芝水 $520", "【Kiehl's】金盞花植物精華化妝水 $750", "【IPSA】美膚微整機能液(流金水) $950"]},
            "step4_essence": {"reason": "平衡皮脂且深層補水精華，讓肌膚油水結構趨於健康穩定。", "items": ["【理膚寶水】B5彈潤修復精華 $950", "【Dr.Wu】玻尿酸保濕精華液 $850", "【Neogence】積雪草B5修護純粹精華 $750"]},
            "step5_cream": {"reason": "補水不補油的清爽凝凍，完美修護雙頰、全天候清爽無負擔。", "items": ["【Kiehl's】冰河醣蛋白無油清爽凝凍 $1350", "【理膚寶水】毛孔緊緻控油保濕乳 $790", "【Clinique】水磁場72H保濕凝膠 $1200"]},
            "step6_sunscreen": {"reason": "醫美級水感高防禦防曬，不致粉刺、全面防禦分區老化。", "items": ["【理膚寶水】全護清爽防曬液 $800", "【Dr.Wu】全效保濕防曬乳 $720", "【雅漾】全效抗UV物理防曬乳 $790"]},
            "step7_base": {"reason": "平衡全臉水油分布的持妝乳，不乾燥亦不浮油。", "items": ["【KATE】零瑕肌密持妝乳 $390", "【Pony Effect】水透光妝前乳 $690", "【MAQuillAGE】心機平衡持妝乳 $720"]},
            "step8_concealer": {"reason": "中高價位全能型遮瑕盤，可自由調配滋潤度、完美隱形瑕疵。", "items": ["【J/X】三色遮瑕膏 $580", "【Excel】完美全效遮瑕盤 $570", "【CLIO】無瑕持妝遮瑕膏 $450"]},
            "step9_foundation": {"reason": "微霧面偏緞面質地粉底，完美隱形 T 字毛孔、服貼雙頰。", "items": ["【Maybelline】反孔特霧粉底液 $420", "【KATE】零瑕肌密微霧粉底液 $540", "【CLIO】柔霧光澤持妝粉底液 $680"]},
            "step10_powder": {"reason": "水潤成膜定妝噴霧，完美鎖住全臉不同區塊的精緻妝容。", "items": ["【1028】空氣定妝噴霧 $350", "【Pony Effect】絕對持久定妝噴霧 $550", "【高絲】美顏定妝噴霧 $360"]}
        },
        "3": {
            "step1_remover": {"reason": "專櫃頂級潔顏油，洗後全臉水油膚感極致平衡、清爽潔淨。", "items": ["【植村秀】抹茶精萃潔顏油 $1500", "【THREE】平衡潔膚油 $1450", "【BOBBI BROWN】沁透茉莉淨妝油 $1350"]},
            "step2_cleanser": {"reason": "天然奢華植物配方，溫和調理並洗淨面部不同區塊皮脂結構。", "items": ["【THREE】平衡潔膚蜜 $1450", "【SK-II】全效活膚潔面乳 $1500", "【香奈兒】深海系列潔顏慕斯 $1650"]},
            "step3_toner": {"reason": "殿堂級神仙水，全面深層調理並強效平衡水油分泌狀態。", "items": ["【SK-II】青春露 $3500", "【ESTEE LAUDER】微分子肌底原生露 $2200", "【LANCOME】超極光活粹晶露 $2500"]},
            "step4_essence": {"reason": "強效修護肌底，調控T字皮脂腺同時深層修護雙頰乾燥脫屑。", "items": ["【蘭蔻】超未來肌因賦活露小黑瓶 $3100", "【雅詩蘭黛】特潤超導修護露小棕瓶 $3200", "【香奈兒】山茶花保濕微導入精華液 $2900"]},
            "step5_cream": {"reason": "高奢輕盈型鎖水水凝乳，輕盈水凝膜科技提供極致分區水分鎖定。", "items": ["【倩碧】水磁場100H活水循環凝膠 $1500", "【Kiehl's】冰河醣蛋白吸油水凝凍 $1600", "【LANCOME】超輕盈雪紡水凝乳 $2000"]},
            "step6_sunscreen": {"reason": "奢華清爽抗老防曬，高滲透成膜技術，全臉輕透無負擔。", "items": ["【肌膚之鑰】無瑕防曬護膚膏 $2500", "【LANCOME】超輕盈UV水凝露 $1950", "【CHANEL】珍珠光感超淨化防護乳 $2000"]},
            "step7_base": {"reason": "專櫃級防脫防裂持妝乳，保濕度足夠且強效對抗T字出油。", "items": ["【植村秀】無極限保濕妝前乳 $1600", "【YSL】名模肌密光燦水凝露 $2150", "【M·A·C】超顯白持妝乳 $1450"]},
            "step8_concealer": {"reason": "頂級高粉體輕盈遮瑕，瞬間霧化T字毛孔並滋潤雙頰暗沉。", "items": ["【NARS】奢華絲柔持妝遮瑕霜 $1100", "【DIOR】超完美持久遮瑕乳 $1300", "【肌膚之鑰】皆效無瑕遮瑕膏 $2000"]},
            "step9_foundation": {"reason": "動態感應持妝科技粉底，面部遇油時更加持妝、乾燥時自動補水。", "items": ["【SHISEIDO】超進化持久粉底液 $1800", "【雅詩蘭黛】粉持久完美持妝粉底 $2100", "【植村秀】無極限超時輕粉底 $1900"]},
            "step10_powder": {"reason": "專櫃經典透明蜜粉，長效控制T字油光且雙頰絕不乾裂起皮。", "items": ["【蘿拉蜜思】煥顏透明蜜粉 $1500", "【M·A·C】超持妝輕透鏡蜜粉 $1500", "【GIVENCHY】高級訂製四格蜜粉 $2200"]}
        }
    },
    "sensitive": {
        "diagnosis": "【敏感肌/泛紅肌學理診斷】\n皮膚物理性與化學性屏障功能嚴重受損。💡 產品挑選關鍵：應嚴格遵循『極簡成分與無刺激學理』，底妝避開酒精、香料、高濃度化學防曬，優先選用物理防曬與礦物成分。",
        "1": {
            "step1_remover": {"reason": "植物性成分基底，配方極度單純，大幅減少界面活性劑物理刺激。", "items": ["【無印良品】敏感肌卸妝油 $290", "【Biore】溫和保濕卸妝乳 $179", "【貝德瑪】舒敏潔膚液(小容量) $220"]},
            "step2_cleanser": {"reason": "不含皂鹼、不含香料，超低刺激性，極致溫和清潔面部。", "items": ["【舒特膚】溫和潔膚乳 $299", "【無印良品】敏感肌洗面乳 $210", "【專科】胺基酸溫和潔顏慕斯 $180"]},
            "step3_toner": {"reason": "單純泉水高安全比例，瞬間舒緩面部泛紅、刺痛與不適感。", "items": ["【雅漾】舒護活泉水 $199", "【理膚寶水】溫和舒緩噴霧 $220", "【理膚寶水】多容安舒緩保濕化妝水 $350"]},
            "step4_essence": {"reason": "無色素香料之極簡保濕精華，給予受損屏障最基礎的安全修護。", "items": ["【無印良品】敏感肌保濕精華液 $390", "【Neogence】積雪草B5修護純粹精華 $750", "【Solone】敏感肌保濕精華 $180"]},
            "step5_cream": {"reason": "提供最單純、不加重防禦負擔的基礎低敏感保濕鎖水乳液。", "items": ["【無印良品】敏感肌乳液 $250", "【CeraVe】修護保濕乳 $399", "【Cetaphil】舒特膚長效潤膚乳 $350"]},
            "step6_sunscreen": {"reason": "純物理防曬配方，零酒精零香料，上臉極度安全、絕不刺痛。", "items": ["【無印良品】敏感肌防曬乳 $290", "【Curel】潤浸保濕防曬乳 $450", "【Orbis】透妍潤色隔離霜 $390"]},
            "step7_base": {"reason": "無添加安全低敏隔離乳，溫和修正泛紅肌膚，不增加負擔。", "items": ["【CEZANNE】長效保濕防曬隔離乳 $290", "【Media】保濕妝前乳 $220", "【1028】舒敏妝前打底乳 $290"]},
            "step8_concealer": {"reason": "通過低敏測試的輕薄遮瑕蜜，安全掩蓋面部紅血絲與泛紅。", "items": ["【Maybelline】FIT ME遮瑕膏 $300", "【1028】服服貼貼遮瑕膏 $280", "【heme】無瑕持久遮瑕蜜 $300"]},
            "step9_foundation": {"reason": "添加溫和礦物成分粉底，對肌膚負擔小，不易引發敏感泛紅。", "items": ["【Media】保濕礦物粉底霜 $280", "【INTEGRATE】柔焦輕透美肌粉餅 $380", "【媚點】自然肌透持效粉底液 $330"]},
            "step10_powder": {"reason": "極簡無刺激成分蜜粉，輕盈定妝，不給皮膚帶來任何化學負擔。", "items": ["【無印良品】敏感肌定妝蜜粉 $350", "【惹我】清爽吸油蜜粉 $145", "【CEZANNE】抗UV保濕蜜粉餅 $290"]}
        },
        "2": {
            "step1_remover": {"reason": "醫美級高效低摩擦舒敏卸妝因子，溫和且高安全溶解彩妝。", "items": ["【理膚寶水】高效溫和卸妝水 $480", "【Curel】潤浸保濕卸妝凝露 $400", "【貝德瑪】舒敏潔膚液 $450"]},
            "step2_cleanser": {"reason": "超細緻綿密慕斯，大幅減少雙手與脆弱肌膚的摩擦物理傷害。", "items": ["【Curel】潤浸保濕洗顏慕斯 $480", "【理膚寶水】多容安泡沫洗面乳 $490", "【Dr.Wu】玻尿酸保濕潔顏慕斯 $400"]},
            "step3_toner": {"reason": "高濃度維生素B5與舒緩成分化妝水，快速壓制泛紅不適。", "items": ["【理膚寶水】多容安舒緩保濕化妝水 $650", "【Dr.Wu】玻尿酸保濕精華化妝水 $500", "【雅漾】舒敏修護保濕精華水 $680"]},
            "step4_essence": {"reason": "醫美核心高濃度B5修護精華，強效加速皮膚物理屏障修復。", "items": ["【理膚寶水】B5舒緩保濕修護精華 $950", "【Dr.Wu】積雪草舒敏修護精華 $900", "【Neogence】積雪草B5修護純粹精華 $750"]},
            "step5_cream": {"reason": "萬用型修復霜，迅速壓制泛紅、粗糙脫屑與突發性刺痛。", "items": ["【理膚寶水】B5全面修復霜 $490", "【Curel】潤浸保濕深層乳霜 $720", "【雅漾】舒敏修護保濕霜 $850"]},
            "step6_sunscreen": {"reason": "100%醫美純物理高防禦隔離防曬，敏弱肌全天候安全無憂。", "items": ["【Avene】雅漾全效抗UV物理防曬乳 $790", "【理膚寶水】全護純物理亮白防曬隔離乳 $850", "【Dr.Wu】低敏物理防曬乳 $700"]},
            "step7_base": {"reason": "專為敏弱肌研發的低刺激持妝乳，築起防護牆、長效持妝。", "items": ["【d program 敏感話題】敏弱飾底乳 $850", "【Curel】潤浸保濕屏護妝前乳 $650", "【MINON】豐潤保濕修飾防曬乳 $600"]},
            "step8_concealer": {"reason": "醫美級抗敏無香料修護遮瑕膏，全面隱形泛紅、絕不刺激傷口。", "items": ["【d program 敏感話題】敏弱遮瑕膏 $600", "【Medicube】修護遮瑕液 $480", "【Nov】娜芙低敏遮瑕膏 $700"]},
            "step9_foundation": {"reason": "專為敏弱與低敏環境設計的溫和底妝，大幅降低化學負擔。", "items": ["【d program 敏感話題】敏弱蜜粉餅 $1100", "【Curel】潤浸保濕屏護粉底液 $750", "【Nov】娜芙礦物粉餅 $950"]},
            "step10_powder": {"reason": "安心溫和舒緩醫美定妝噴霧，有效減少全臉化學乾粉物理負擔。", "items": ["【理膚寶水】多容安舒緩修護噴霧 $750", "【雅漾】舒護活泉水噴霧定妝 $450", "【Curel】潤浸保濕微粒子噴霧 $550"]}
        },
        "3": {
            "step1_remover": {"reason": "頂級草本低敏植物油，在極致安全無刺激下溶解防水彩妝。", "items": ["【DARPHIN】全效舒緩卸妝乳 $1500", "【THREE】平衡潔膚油 $1450", "【植村秀】抹茶精萃潔顏油 $1500"]},
            "step2_cleanser": {"reason": "高奢極致溫和胺基酸洗顏，徹底淨化同時完美撫平脆弱肌理。", "items": ["【THREE】平衡潔膚蜜 $1450", "【SK-II】全效活膚潔面乳 $1500", "【香奈兒】深海系列潔顏慕斯 $1650"]},
            "step3_toner": {"reason": "貴婦級修護精華水，富含神級穩定修護因子，根治敏感。", "items": ["【SK-II】青春露 $3500", "【LANCOME】絕對完美玫瑰修護露 $2800", "【LA MER】濃縮精華露 $3500"]},
            "step4_essence": {"reason": "殿堂級植萃舒緩神級精華，徹底阻斷物理與化學發炎刺激。", "items": ["【DARPHIN】全效舒緩精華小粉紅 $2500", "【LA MER】濃縮精華 $4500", "【蘭蔻】超未來肌因賦活露小黑瓶 $3100"]},
            "step5_cream": {"reason": "傳奇專櫃頂級屏障修護乳霜，提供神級修護力，讓脆弱肌原地重生。", "items": ["【海洋拉娜】經典乳霜 $6800", "【倩碧】水磁場72H保濕凝膠 $1500", "【百優】精純乳霜 $2300"]},
            "step6_sunscreen": {"reason": "頂級奢華物理抗老防曬，細緻輕盈，全面阻斷敏感泛紅惡化。", "items": ["【肌膚之鑰】全效防護乳 $3300", "【CHANEL】珍珠光感超淨化防護乳 $2000", "【DIOR】雪晶靈輕透防曬隔離乳 $2200"]},
            "step7_base": {"reason": "明星級全能安全打底妝前乳，修飾泛紅並平衡面部屏障結構。", "items": ["【蘿拉蜜思】煥顏凝露(經典型) $1500", "【肌膚之鑰】光采無瑕妝前凝霜 $2100", "【植村秀】無極限保濕妝前乳 $1600"]},
            "step8_concealer": {"reason": "高奢養膚型保濕遮瑕，極致輕盈貼膚，完美隱蔽泛紅微血管。", "items": ["【肌膚之鑰】皆效無瑕遮瑕膏 $2000", "【NARS】奢華絲柔持妝遮瑕霜 $1100", "【LA MER】奇蹟煥采遮瑕膏 $2500"]},
            "step9_foundation": {"reason": "專利動態修護持妝科技粉底，高遮瑕且將對敏弱肌的負擔降至最低。", "items": ["【SHISEIDO】超進化持久粉底液 $1800", "【BOBBI BROWN】冬蟲夏草精華粉底 $2600", "【植村秀】無極限超時輕粉底 $1900"]},
            "step10_powder": {"reason": "專櫃奢華極細透明蜜粉，完美柔焦，對敏弱肌膚極致零摩擦。", "items": ["【蘿拉蜜思】煥顏透明蜜粉 $1500", "【香奈兒】輕盈完美蜜粉 $2150", "【肌膚之鑰】光采蜜粉 $2450"]}
        }
    }
}

# ==============================================================================
# 🎨 2. 風格彩妝推薦資料庫 (STEP 11 ~ 13)
# ==============================================================================
MAKEUP_STYLE_DATABASE = {
    "1": { 
        "style_name": "韓系暖調大地色系妝容",
        "budget_data": {
            "1": {"eyeshadow": ["【1028】飛我莫屬限量眼彩盤 #杏影大地 $390", "【heme】六色眼影盤 #大地 $299"], "blusher": ["【Romand】勝過完美腮紅 $260", "【heme】純色腮紅 $240"], "lipstick": ["【Romand】果汁水光唇釉 $280", "【1028】野熟唇釉 $290"]},
            "2": {"eyeshadow": ["【CLIO】璀璨星沙十色眼影盤 $680", "【3CE】九色眼影盤 #DEAR NUDE $790"], "blusher": ["【3CE】單色腮紅 $450", "【M·A·C】持色奶凍腮紅 $750"], "lipstick": ["【3CE】絲絨霧面唇釉 $490", "【M·A·C】子彈頭唇膏 $800"]},
            "3": {"eyeshadow": ["【TOM FORD】高級定製四格眼盤 #03 $2600", "【CHANEL】四色眼影盤 $2100"], "blusher": ["【NARS】炫色腮紅 $1150", "【DIOR】藍星腮紅 $1450"], "lipstick": ["【DIOR】癮誘唇膏 $1400", "【YSL】奢華緞面絨霧唇膏 $1450"]}
        }
    },
    "2": { 
        "style_name": "溫柔玫瑰粉棕色系妝容",
        "budget_data": {
            "1": {"eyeshadow": ["【heme】六色眼影盤 #玫瑰蜜桃 $299", "【Canmake】完美高效眼影盤 $380"], "blusher": ["【Canmake】花漾戀愛修容組 $390", "【Romand】完美腮紅 $260"], "lipstick": ["【Romand】果汁水光唇釉 $280", "【CEZANNE】持久潤澤唇膏 $260"]},
            "2": {"eyeshadow": ["【3CE】九色眼影盤 #OVERTAKE $790", "【CLIO】十色眼影盤 #櫻花粉 $680"], "blusher": ["【Clinique】小雛菊腮紅 $700", "【3CE】單色腮紅 $450"], "lipstick": ["【M·A·C】絲柔粉霧唇釉 $1050", "【Pony Effect】奢華唇釉 $550"]},
            "3": {"eyeshadow": ["【SUQQU】晶采盈緻眼彩盤 $2600", "【DIOR】經典五色眼影 #玫瑰色 $2500"], "blusher": ["【CHANEL】圓形腮紅 $1500", "【NARS】炫色腮紅 $1150"], "lipstick": ["【Tom Ford】設計師唇膏 $1900", "【CHANEL】COCO晶亮水唇膏 $1400"]}
        }
    },
    "3": { 
        "style_name": "輕歐美俐落消腫冷灰棕妝容",
        "budget_data": {
            "1": {"eyeshadow": ["【Solone】經典單色眼影自組盤 $250", "【1028】飛我莫屬限量眼彩盤 #灰調 $390"], "blusher": ["【heme】純色腮紅 #04 $240", "【Solone】經典腮紅 $150"], "lipstick": ["【into you】唇泥 #EM23 $249", "【Solone】極潤緞光唇膏 $280"]},
            "2": {"eyeshadow": ["【KATE】色影迷棕眼影盤 $420", "【3CE】九色眼影盤 #SOME DEF $790"], "blusher": ["微【3CE】單色腮紅 $450", "【Clinique】小雛菊腮紅 #修容色 $700"], "lipstick": ["【MAC】時尚唇膏 #Taupe $800", "【3CE】絲絨霧面唇釉 $490"]},
            "3": {"eyeshadow": ["【DIOR】經典五色眼影 #酷灰 $2500", "【TOM FORD】四格眼盤 #消腫灰 $2600"], "blusher": ["【NARS】霧光修容餅 $1400", "【CHANEL】圓形腮紅 $1500"], "lipstick": ["【YSL】小黑條口紅 #314 $1450", "【DIOR】巨星唇膏 $1400"]}
        }
    },
    "4": { 
        "style_name": "白開水偽素顏輕透妝容",
        "budget_data": {
            "1": {"eyeshadow": ["【Canmake】完美霧面眉影盤 $380", "【heme】六色眼影盤 #純淨 $299"], "blusher": ["【heme】純色腮紅 #10 $240", "【CEZANNE】單色腮紅 $180"], "lipstick": ["【CEZANNE】持久潤澤唇膏 $260", "【OPERA】金管唇膏 $380"]},
            "2": {"eyeshadow": ["【Excel】裸色深邃眼影盤 #SR01 $535", "【KATE】色影迷棕眼影盤 $420"], "blusher": ["【Clinique】小雛菊腮紅 #18 $700", "【3CE】柔霧腮紅 $450"], "lipstick": ["【OPERA】柔潤唇膏 #05 $380", "【M·A·C】子彈頭護唇膏 $800"]},
            "3": {"eyeshadow": ["【BOBBI BROWN】時尚奢華眼影 $1300", "【SUQQU】晶采盈緻眼彩盤 $2600"], "blusher": ["【SUQQU】晶采淨妍頰彩 $2100", "【DIOR】藍星腮紅 $1450"], "lipstick": ["【CHANEL】COCO晶亮水唇膏 $1400", "【DIOR】豐漾俏唇蜜 $1350"]}
        }
    },
    "5": { 
        "style_name": "早八快速妝容",
        "budget_data": {
            "1": {"eyeshadow": ["【Solone】單色霧面消腫眼影 $110", "【Canmake】雙色快捷眼影 $250"], "blusher": ["【heme】純色腮紅 #10 $240", "【惹我】清爽腮紅 $160"], "lipstick": ["【OPERA】柔潤唇膏 #經典色 $380", "【CEZANNE】持久潤澤唇膏 $260"]},
            "2": {"eyeshadow": ["【KATE】雙色亮片眼影盤 $360", "【1028】飛我莫屬限量眼彩盤 $390"], "blusher": ["【M·A·C】持色奶凍腮紅 $750", "【3CE】液態腮紅 $450"], "lipstick": ["【I'M MEME】我愛心機水光唇萃 $390", "【Romand】果汁水光唇釉 $280"]},
            "3": {"eyeshadow": ["【BOBBI BROWN】流雲持久防水眼影筆 $1200", "【LAURA MERCIER】夢露煙燻眼影筆 $1100"], "blusher": ["【NARS】多功能彩妝膏 $1350", "【CHANEL】泡泡腮紅 $1750"], "lipstick": ["【DIOR】癮誘粉漾潤唇膏 $1350", "【CHANEL】COCO晶亮水唇膏 $1400"]}
        }
    }
}

TUTORIAL_DATABASE = {
    "skincare": [
        {"title": "皮膚科莊盈彥醫師 - 基礎護膚學理與正確保養順序", "url": "https://www.youtube.com/results?search_query=%E8%8E%8A%E7%9B%88%E5%BD%A5+%E4%BF%9D%E9%A4%8A%E9%A0%86%E5%BA%8F"},
        {"title": "Dr. Ivan 6 - 混合肌與油肌分區控油穩膚防脫皮教學", "url": "https://www.youtube.com/results?search_query=Dr+Ivan+6+%E6%B7%B7%E5%90%88%E8%82%8C+%E4%BF%9D%E9%A4%8A"}
    ],
    "makeup_styles": {
        "1": {"title": "PONY - 韓系日常大地色消腫暖調妝容完整教學", "url": "https://www.youtube.com/results?search_query=PONY+%E9%9F%93%E7%B3%BB%E5%A4%A7%E5%9C%B0%E8%89%B2%E5%A6%9D%E5%AE%B9"},
        "2": {"title": "一枝南南 - 溫柔玫瑰粉棕色大面積腮紅招桃花約會妝", "url": "https://www.youtube.com/results?search_query=%E4%B8%80%E6%9E%9D%E5%8D%97%E5%8D%97+%E7%8E%AB%E7%91%B0%E7%B2%89%E6%A3%95%E5%A6%9D%E5%AE%B9"},
        "3": {"title": "Jcnana 蒨蒨 - 亞洲面孔消腫冷灰棕妝容與輕歐美結構修容術", "url": "https://www.youtube.com/results?search_query=Jcnana+%E5%86%B7%E7%81%B0%E6%A3%95%E5%A6%9D%E5%AE%B9"},
        "4": {"title": "鴨鴨 Makeup - 低粉感、低飽和無心機『白開水純欲妝』核心教學", "url": "https://www.youtube.com/results?search_query=%E9%B4%A8%E9%B4%A8+Makeup+%E5%85%AA%E9%96%8B%E6%B0%B4%E5%A6%9D%E5%AE%B9"},
        "5": {"title": "早八快速完妝教學 - 5分鐘俐落出門防遲到快速彩妝術", "url": "https://www.youtube.com/results?search_query=%E6%97%A9%E5%85%AB+%E5%BF%AB%E9%80%9F%E5%A6%9D%E5%AE%B9"}
    }
}

# ==============================================================================
# 📺 3. Streamlit 網頁介面設計
# ==============================================================================
st.set_page_config(page_title="專業級智能美妝護膚諮詢系統", page_icon="💄", layout="centered")

st.title("💄 專業級智能美妝與護膚諮詢系統")
st.write("精準分析：提供『妝前保養、完美底妝、風格彩妝』一站式客製化學理護膚指南。")
st.markdown("---")

st.header("🔍 請輸入您的個人條件")

# 模式切換開關
mode_option = st.radio(
    "💡 請選擇系統運作模式：",
    ["🌞 13步精緻全妝指南 (日間保養+底妝+彩妝)", "🌙 5步深夜保養修護 (夜間清潔+深度鎖水)"],
    index=0
)
is_night_mode = "5步深夜保養修護" in mode_option

skin_options = {"油性肌/痘痘肌": "oil", "乾燥肌/缺水肌": "dry", "混合肌": "mix", "敏感肌/泛紅肌": "sensitive"}
user_skin_label = st.selectbox("1. 您的主要膚質是什麼？", list(skin_options.keys()))
user_skin = skin_options[user_skin_label]

budget_options = {"💰 小資學生黨 (低預算)": "1", "💎 稍微有預算 (中預算)": "2", "👑 精緻高級小奢華 (高預算)": "3"}
user_budget_label = st.selectbox("2. 您的預算級別？", list(budget_options.keys()))
user_budget = budget_options[user_budget_label]

style_options = {
    "✨ 韓系暖調大地色系妝容": "1",
    "🌹 溫柔玫瑰粉棕色系妝容": "2",
    "🕶️ 輕歐美俐落消腫冷灰棕妝容": "3",
    "🥛 白開水偽素顏輕透妝容": "4",
    "⏰ 早八快速妝容": "5"
}

# 當切換至深夜保養時，動態禁用彩妝風格選單
user_style_label = st.selectbox(
    "3. 您今天想搭配哪一種彩妝風格？", 
    list(style_options.keys()), 
    disabled=is_night_mode,
    help="當切換為『深夜保養修護』模式時，此選單會自動禁用。"
)
user_style = style_options[user_style_label] if not is_night_mode else "1"

# 按鈕文字隨模式自動更換
btn_text = "🚀 生成夜間深度保養修護報告" if is_night_mode else "🚀 生成客製化 13 步美妝護膚報告"

if st.button(btn_text, use_container_width=True):
    st.markdown("---")
    
    skin_info = SKIN_DATABASE[user_skin]
    skin_dict = skin_info[user_budget]
    
    if is_night_mode:
        # ==========================================================================
        # 🌙 模式 A：深夜保養修護報告 (5 步驟) -> 從卸妝潔顏開始，完全符合夜間邏輯
        # ==========================================================================
        st.header(f"🎉 您的深夜保養修護報告")
        st.info(skin_info["diagnosis"].replace("底妝", "保養"))
        
        st.subheader("🧴 核心修護階段：深夜保養 (STEP 1 ~ 5)")
        night_steps = [
            ("STEP 1【深層卸妝/洗卸步驟】", "step1_remover"),
            ("STEP 2【溫和潔顏步驟】", "step2_cleanser"),
            ("STEP 3【二次調理/夜間化妝水】", "step3_toner"),
            ("STEP 4【高濃度密集精華修護】", "step4_essence"),
            ("STEP 5【最後鎖水厚敷乳霜步驟】", "step5_cream")
        ]
        for step_title, db_key in night_steps:
            with st.expander(step_title, expanded=True):
                st.markdown(f"💡 **夜間學理修護理由**：{skin_dict[db_key]['reason'].replace('妝前', '夜間')}")
                st.markdown("**📋 推薦符合此條件的品項：**")
                for item in skin_dict[db_key]['items']:
                    st.write(f"- {item}")
    else:
        # ==========================================================================
        # 🌞 模式 B：精緻全妝指南 (13 步驟) -> 導正盲點：日間化妝前「不從卸妝開始」，改由化妝水起步
        # ==========================================================================
        st.header(f"🎉 您的 13 步客製化報告 ({user_style_label})")
        st.info(skin_info["diagnosis"])
        
        style_info = MAKEUP_STYLE_DATABASE[user_style]
        raw_makeup_lists = style_info["budget_data"][user_budget]
        
        # 🧴 PART 1：日間妝前保養篇 (STEP 1 ~ 3) -> 從化妝水開始
        st.subheader("🧴 第一階段：日間妝前神級保養 (STEP 1 ~ 3)")
        skincare_steps = [
            ("STEP 1【基礎補水/化妝水步驟】", "step3_toner"),
            ("STEP 2【高效密集保濕精華步驟】", "step4_essence"),
            ("STEP 3【輕盈鎖水修護乳霜步驟】", "step5_cream")
        ]
        for step_title, db_key in skincare_steps:
            with st.expander(step_title, expanded=True):
                st.markdown(f"💡 **學理推薦理由**：{skin_dict[db_key]['reason']}")
                st.markdown("**📋 推薦符合此條件的品項：**")
                for item in skin_dict[db_key]['items']:
                    st.write(f"- {item}")
                    
        # 🪞 PART 2：完美底妝篇 (STEP 4 ~ 10) -> 步驟重新依序順延編號
        st.markdown(" ")
        st.subheader("🪞 第二階段：極致服貼底妝 (STEP 4 ~ 10)")
        makeup_base_steps = [
            ("STEP 4【日間高效防曬步驟】", "step6_sunscreen"),
            ("STEP 5【隔離打底/校色飾底乳步驟】", "step7_base"),
            ("STEP 6【局部瑕疵/重點遮瑕步驟】", "step8_concealer"),
            ("STEP 7【全臉無瑕粉底上妝步驟】", "step9_foundation"),
            ("STEP 8【蜜粉定妝/噴霧定妝鎖水步驟】", "step10_powder"),
            ("STEP 9【立體輪廓/修容高光步驟】", "step10_powder"), # 使用原本定妝或底妝基底，增加全妝精緻度
            ("STEP 10【精神元氣/完美眉彩步驟】", "step10_powder")
        ]
        # 備註：此處為了不破壞妳原本設計的 10 大資料庫結構，STEP 9與10共用粉體延伸，但顯示標題重新定義為彩妝基本功
        for step_title, db_key in makeup_base_steps[:5]: # 前五個核心底妝防曬步驟
            with st.expander(step_title, expanded=True):
                st.markdown(f"💡 **學理推薦理由**：{skin_dict[db_key]['reason']}")
                st.markdown("**📋 推薦符合此條件的品項：**")
                for item in skin_dict[db_key]['items']:
                    st.write(f"- {item}")
                    
        with st.expander("STEP 9【全臉精神元氣/完美眉彩步驟】", expanded=True):
            st.markdown("💡 **學理推薦理由**：在進入彩妝前，優先勾勒出眉型輪廓，能讓整體的五官立體度與精神感瞬間提升，也是精緻妝容不可或缺的骨架。")
            st.markdown("**📋 推薦品項：** 建議搭配個人髮色選擇市售抗汗眉筆或眉粉。")

        with st.expander("STEP 10【精緻面部輪廓/修容高光步驟】", expanded=True):
            st.markdown("💡 **學理推薦理由**：利用陰影與高光粉體修飾臉部立體結構，讓後續的風格彩妝色彩呈現更加生動、立體不扁平。")
            st.markdown("**📋 推薦品項：** 建議選擇偏灰調修容與細緻不顯毛孔的高光盤。")

        # 🎨 PART 3：風格彩妝篇 (STEP 11 ~ 13) -> 精準承接後續彩妝大作
        st.markdown(" ")
        st.subheader("🎨 第三階段：彩妝精華點綴 (STEP 11 ~ 13)")

        with st.expander(f"STEP 11【{style_info['style_name']} - 風格深邃眼妝】", expanded=True):
            st.markdown(f"💡 **學理推薦理由**：依據『{style_info['style_name']}』色彩美學，加強眼部消腫與立體輪廓。")
            st.markdown("**📋 推薦眼影品項：**")
            for item in raw_makeup_lists["eyeshadow"]: st.write(f"- {item}")

        with st.expander(f"STEP 12【{style_info['style_name']} - 氣色雙頰腮紅】", expanded=True):
            st.markdown(f"💡 **學理推薦理由**：依據『{style_info['style_name']}』大面積暈染，完美修飾臉型並提升整體氣色。")
            st.markdown("**📋 推薦腮紅品項：**")
            for item in raw_makeup_lists["blusher"]: st.write(f"- {item}")

        with st.expander(f"STEP 13【{style_info['style_name']} - 唇部點綴唇妝】", expanded=True):
            st.markdown(f"💡 **學理推薦理由**：依據『{style_info['style_name']}』色調，勾勒完美唇形，達成全妝視覺收尾。")
            st.markdown("**📋 推薦口紅品項：**")
            for item in raw_makeup_lists["lipstick"]: st.write(f"- {item}")

    # ==========================================================================
    # 📺 共通區塊：影音教程推薦
    # ==============================================================================
    st.markdown("---")
    st.subheader("📺 專屬線上影音教程推薦")
    
    st.markdown("**【基礎保養學理教程】**")
    for link_item in TUTORIAL_DATABASE["skincare"]:
        st.link_button(f"🧴 {link_item['title']}", link_item['url'])
        
    if not is_night_mode:
        st.markdown("**【本次彩妝風格教程】**")
        style_tutorial = TUTORIAL_DATABASE["makeup_styles"][user_style]
        st.link_button(f"🎬 {style_tutorial['title']}", style_tutorial['url'])