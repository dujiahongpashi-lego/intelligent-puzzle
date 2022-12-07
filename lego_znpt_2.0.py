# 需将压力传感器接入F，按压力传感器切换题目
from mindstorms import ForceSensor
from mindstorms.control import wait_for_seconds
from mindstorms import MSHub
import random
a1 = [0x82f40204e27b3b42f70002ea5d86b04700d0121d0bb04700d002e43fb04700d002e34596406d700d220b829e68a00efb16b0360d501105b8b0d888d0056b8ba037402022ccdca0f648d020890b69986d1024c5e596dc6e0022c1b2b04f00a029d78296c628d0125d0b96c06d7002ca24b0c3014014253a8ec668a0115d2a96c46c7002fa4596c46e40052a2b16c3414016256716c74550160a4a831b41400d9867a0364dd002e13143806ea0042b0b43806ea00405a643986e00042b0b829268a004232f968a08a0042221b0820d5004223f,
0x43813ab1e18c0543813dd0c62d9440a46cdec5025740a46cdec503578280684ec2e6df8280684ec2e7cd82806cdec10a2b82823ab1e18c059684685e02f219a8820dd0c62205a0805841f12cc0b0805841f12bc097406a7e05022b10550e0ecfdc0410550e0ece750417590e0ed1024c08350e0ed99ddf0b590e0ed21d450d810ea1e95e8597810970c16a44118108588d2a3f561b06a5341385b0130291f416a7a0db4140162010829268a004a32f8e9268a004a02f828a68a004a321179a4510e26a85a85a6d10cda305a81a6d16c9a305,
0x96c06d74010a2b2b808eaa001508b0d300b1e851d4969a0a00c622142a37421ac2c267b0170211f40418b0d30211f4069b96418aae00320810c0860ec0355297406b4e02d1b12158460ec017c42158460ec017c52198460a80222921133607e004b8218046aac0222921825c47e004b82100460ec0332948f608d2002d8810573607e019b1b0570081e019b1b0570381e019b110574626201cb310574626201fb39780681a010a2b22f700a009a816b03608161105f4238268a0142d96b03700016869239780681a02c24482f4084531ddf8,
0x17826b1012ea4617826b1012e25406e66e0031c4bc45981600341fba10e705d034090410e705d0342104b0db0140340186b0cb0140340186b00f00a03417ad97806830340346718046a034143396886d1030811210f5cd103d0904b054451024d484b094451024d7f4a81a6d1025518382a668a011c8f8839a30a00bc893839a30a00bc8a38e360dd011488b968a08a00488c696dc6e0002c82010f5cd103d0902a0f648d010082196c46e4002c8228e360dd0114590968a08a004ba11978108a004922f4b9a08a004ad65b0370120084599,
0x1682684e12e1d116826c1e12c2144180c6a0d41f944181c0aa0a0a04b0c528a0049491968a08a004a211a0a668a00490f88ac540a004a520438026a1e3535c4380eea0d62305423426ae15b2609685a8ae0e24aa9684689e0143b616820cded14a06a08343a8160a06a08268477024bca0824dd0d00a4ca08344a0d00a4916866d4e11026b1086685e191abc08846d4e0d2544179a0c601148a396486d10045b4616826e00043b4116c66a40114a7808f700d020ddc3a01740d024df88043595d022ebcb968810a030abe9969810a0326bc4,
0xb01c6a3022ebca8e349dd022c1098e3495d022c13696886d10308b0670574626201999b05446262019a9105716a62019b9829268a2003b2f969238a200202f964990d2201d084e3725d200280b658880a62004da538044222017eb4d98410ac017e5578216a220098b658085d1e018dbb037012220058996486e022019887188410620132c10d20917e02ad796560915201d0910c88536201fbd20260db7e016c4218206a1e01c5c22e705d2e004d222db40dac0136722f4451760132c22a442dec00bd722dc43d7601417b04700a88017d4,
0xb04702d2a00b08b0470351e00c084a470687e00a5aa844ab87e02e89105706a728d88482426aa600230b8aec4517e0154092430357e01c30b037035168d8b928f648d62111c4a0144687ea11b12340689e0013ccb0444602a02bcc5644460ec03514a8444157e02ec4b04442d4a02b946a4446a4c03a14b0444276a02b94222700d2e02cd0222702d2e02869b03700416851d2969a0a00c622058a4446a4c01a1482dc43d7601417a09844a8002ceb10f648562d3923a0e443d4c02037a0f488d3602208a0348dd7602c941158860ec0253a,
0x1199c60ac013c51159c40ec013e510f60b92e022f416426b36203b361645be0ec01a8910466e02a01d1710470687e01acd10470157e0347808ef00d7e8d8e98234220731d5a697406a1e0d05c697406a1e02c2142a374213612bdc97806a1a02e2045214421eda1fd77014421eda1457578216a0c84d234558684ec2d0ca82f638d602eda08a360ea16cad2196886c1e0503210b133607e8d0ba441b32b7f5908508d290de0851bf0b133607e859bab01302b1e851d40b825c47e859ba7180c6a0c8691496c06d7405022bb03426262814ab,
0x978210d6c842a3839a3201ed86850b426a1e12dd46828820d7f36321a01740a13611a1acd0a0d7e111a1a4c868462885cc08ee08d7ecba21a8360dd65102a1b02f0041e818a9b05b0380c842bfb0130291e856a4821a6a06ca3b0570c740d6e16aa0825a3ea0cc82a108ef00d7f25ba017826b4a12d0a3118246a2ee1004b0130351e851a4b0130211f415bd161702173404ca10170217f41c4a08d30211f406d942f700a2002b2cb0370292201112b02702d2201114a0a668a20010f850c528a2002ca0b0c628a20017a0a8c668a20012a0,
0x828a68a2003b21828a68a200232160e70147e01eed61984604c01f94b0c45d51e00a4a96c44644801d144d98460ac01794569c460ec035146d984604c01f944d98430ac0179410958eae001c9410f72392200954b0d441222019af10d741222019cf820913dec0556c82086a6ec063df82086cdec051348318689640737882181adec0533683981b6ac057ad82f418d7605bc9835818dec05b46825c1ea0c04d5a825c1ca0c07378825c1ca0c07b6882581b60c05ecf829015d1e063238288402ec056bf8288402ec057bd8288682ec067d7,
0x83986836406b46829c402ec06d6a829cd821e044768298402ec067dd8358402ec057ad83984024c05fcd8249b5d04057b2104f4602202b9710e705d2202914b0cc4106202bc6119a0916a01fcd10560917e03478b0c44102e017b5119083b7e018b311888336201ecf10d8830ec0335610548d17e0327610548d17e01c78a0a668a20013f8b02702d2201112b02700d220111210f7059220111210e705d22029128358411ec017b7b04f0272200b0810e705d220092210e70122201fcd1181c6a2202c13118213d2202db810e669062013bc,
0x10f6091760129710da0914a03a1716de0916a0250910d20917e02eeb10560917e03c6a10c33107e02b1710c72107e02e9711808397e018cd11908407e0184db02482d620396210c886a6202cbc11808317e02ddd10548eae0032398a508d11e01a0a96548d17201d09100e6e0025e83c10f70020342dd9100f06a03403d91057451024df841713451024da4fb054451024c1398ef4451031412ca8f4451030812c5054451020ec841057451020df8469986d1020c2e59690451020fa2fb095c51020c4f416de6d1012e06516426d10117b36,
0x96086d102911e9b00c451029d787b00c6d10320347100e6d1032c3baa0f443902a0112a0f443902a0902a03425d02ad483079842802be14d06344ea035a342499820d020eb5c8e344dd021c185579840502a5b83824a68d0405d32839a3190405fad839a3280405f9896886c1e0043168e88edd0c060168e8a69d0c06016ac1e08d7f1400b769e08ded1400ba8350dd206c008b04f006229c03f6ac4e940c6c074b0c4ed50c540169698402630c0c47188c0262200d4a8f4c0262200d3578810a62a40d2b0d8c6262200d404b703117e00e8,
0xb0570311e0809304db40d636008b96ccc5762200bca474cb262200db514843263e00f2578a10a62240b49298186633c0c48688682633c0fa968868263c80c9908868263e00c2969840263240c4500b42563600a3480b42d63600a34a0b15d628c0db560916a630c0c6500b46263600d2500c45d625c0d2ac0c686633c0d20e0c6dd63180d20589c3263580d2078845d62a40c3071b46262240baa874cd10c400216d9118d7e44012761c9e0ec440508a820ea202001fa0364dd202c0066434964226c008b0360d5202c006a8c4edd0c5003b,
0xa8f4c510c4401496499510c4403a9698420e040060b09588a13c0007828042aec4006c8a820ea0c4004b90570310de001992570310d3c01990570310de001f8af448d232c043961c6c0e02c0604d904407f5800780774110dc001ba8760910c6c0440d82690763c03096598100ce0050569e086ed1406ab036087171406796de0864d1403c4d5a18aed0403f97004646c98007a074cd90d000276eb4860ec2001ca0ac88a5fe00592af489a762007668c73107eb40655180412236006b643705d232c069461b029233c012839a4242020047,
0x16426d1012e23416426d10193a4b219a0bd0116b19239a46000e283796180d78015d2c10c403a6a82be9a01b4004cd9fc6a0374000ea55da6ef60806a8bb2196c46810b25b47b0c44014add7f4b0c44012e95784a01440172a253ca0f548a0100bac839884600c1d29b0c5c10005da99a00f40a03613afa00f40a02bd3aaa00b40d0289fb3a0f418d0309b78a0181ab032613fa0f440202a5daca0c8402029aca2a0c840202a2ca2a01a6aa02a65f8a01b43a0361529a0195ea02bd1d9a01b43d02ad1aca0a668a0208a78539845102bd965,
0x8277411362006792d60917e2403a92d48510d3c02f9019410ec9c06430d48510de00491398848623c04f30d48310de005fb0348862bc005728348dde12c00828f48d10dd004b96c4835723c03a0f0b00d7f340410eb61c9ed040570f106eae18804f2eb60d6ed14008a0ac8865fe00593798be0ac200450f106e0eda004f4e1b0407b3c02fa0ec8a47f24044826f4111e1806782523ba602001fa06743d0c40031a0e669d0c400316d904317ea00c56d984316aa00cf62086eae0900e662d8c5de0200d783185e6603c093839a30a60bc093,
0x8ec66940d14034a8c445d0e5402fb0c4ed50c5404692c629d0d3c025705316a622001f5740421e04006b829044dec4002f2664edd0c4405710ee0e47e4002410960ba724007470534320d0401fb0c628d6d20025b051c606e2001f28c669d0dd005528c46d5893c00816c724a20880060c4f25d223c03d179a46022240170ce705d223c04c318246a22200072d923100d3c01f9740834e03c03a30d48310d2404c10948e87fc000710948eae0e400728b48d1ed140080f0b25d1a3c041161e1cbed0405f0f0b10d7f0403d8a6e0970d3c01f,
0xa8d20dd1e0498a96886c1e004904b0d300b1e049d44e741ea0c06018968a39d0c04b4060f7009732c0ac603705d122c0cb4ac740d0450093b0c30091f4009d631b40d6dc008860f700972ec0ac60a700d7ef40f860f700d56a40f8607706a72200bb603700272900bb96c4164483c0bab0c4ed50c6c09604c305da0ec0f804c300aa1e00ab60a70081fe00ad96c0450e0a00ba04c5a8b723c0f470c74096adc0ac4cc435d1f140a576c0c12ec2008404af00a5fe00d6965f01b083c0e904dc6e0373c0cd04adbe01fe00df05586e0ec2c0ca,
0x10c744a6d140e730c66950d2c076164c3c723e0074104dc60221c056164f00723e0059111a1ea6d04007310a6e60d04027139a4600e3c0540ce66e06e3c04596d468972059c152d74081e059c1960e39d0c06ac1960e3876c06ac1a80cbdd0c04d41b0d608a120412388760990c07b02b0560881e04984b034cd104060478c98402ec067c0059158a7e05cc110f59607606a416d9018d7e06840978042aa0041c088f41d10c07b400758460ec062299690441e0049afb00b03848057c14c120dd1e06d83460b06a520554110f41e00e06840,
0x05586e0ec6c0cc4ef72030c5809f05806b1373c0cd6e486b0ec080ec138186aa03c0c860256eac1c00d804c558a5fe00e804c2b0a5fe00ca055980bec3c0cc055980aed200b8b01d88a0bc0083099a08d61140830551851e93c0bcb0198a70bc008396118a4e03c08356098eae0880b604c2a517fd00ed621a6aae0880b662d895de0080d708b5be0ecec09396c638d6cd40a2561b4606e880b92ec669d6a2008462086ea45c00e60cc66836a3c0e7a00980d44e40f8a0198687e880aca04983a722008208b5ce06fe009310c5e82ed140b8,
0x97005e0603c09306a5e8d63e00c204cb40b623c0d80435959622c0dc04f60c561d00bb050b43d62d00e3a40a5a8633c0af662742d63600f2662742d63600f411120e4613c0bc11120e4613c0baacd01317e880d5862742d63600b286181ba63240ac84181a663e00f2461946263e00d9461b46262a00cf461b46262a40dc10f724662d00e3171b46262240b2170b46262240b210f713263500eb69996e006045d0b015c5506044c108d740d0605fc1719a0600405519a82c15d1e051c1968a09d0c04b76968a09d0c04b4625806c40404dcc,
0x8ef41d10c060654eb4402ec06068b0d30031e046d408b5a56ec041c0042e0601e05cb210ee0e47e0498410d20db7e04984a82e0dd1e0498210d60e87e0438210560ea720412310960ea72041f4b01a0d50a041ac171a0e66a041b608360e476041dc08d608d72041eb08d60ea72041ac11920bb7e041398a1a0ea4c05a23965a0b40c05d2382656ea04063f683986990406358829a6930404b4683186ea04049ab83986ca04049ab83186ea0404d938288686ec067dd828a69d0c04b46828a69d0c07b188219422ec067d7831b40a64041e7,
0x56820ea2403a084f996d12402a88b0d30121e008d4a88045d8000850968810ae0061d1978068964068429690402e0051af9688686e0064c1b05445106057849690251060622f059990aac0652f969c42a06052f6968810ae0064d110950ea720087410950e87e00874829045d8c0082f86e445d620151110d33127e02c1182984208c0097656dc46a4000935829045d8c0092fb0d608a1200924221c6cdec6c057239a42a0c580472276a510dd00182036c29ed04072211b4620d0402f22e669d0c5c06720344c3ed040722074cd90d04044,
0x829024dec041af829025d8c041af82d845d4c041a582886dd8c0411482763ea0c05d8283996c60c04c0282a5e8dec06384829044dec049af8088682e0065598088686e0064cc06ee08d7e06229a8360dd040623b968a09d0c04b7496886c1e000921b05445106054849688682e0064d1969c6a0e00082bb0570081e008a3b0560881e008a310960e87e00874a80c3511e053dca00c46a4c06c8786374296202d1182886cdec0091182886c7ec0091196886d180009119698420e000940a0f4b8d3600808a0d04127e0151182a5e8dec02391,
0x059968a62ad98150d44052686f819098402ec87801501446aac0d081b0d188b1fc0181b09588a13c018107132513e21081a834cdd0484901683725d0684281500c45b0e86f81a80e69d0c84b016234483ec1f80151984602f601017700c606023d01059a08b61147815198430ac5c1010435ce263e058104b5ce263e0581969818663ca481066743d622210117120e4613c1816e49eb0ec201017609bb0ec895010cd18831fc2f8196098aae089a016a098aae08a50196086e44485981b00c4550e85781a80c45d0e857810559c32ec86a81,
0x20e669d0dc00512064edd0d0404222de6e00d2c052223705d7748069225b43d0dc0051231b40d6dc0051221f03aa1e0068238036aa03c02d22f4c500dc001783584adec02321229c32bec3c04f22d846a4d5800722ecc577e2000722e4b3d6e2001fb0470351e1801a964700d6c54069ac45b602b3c02f4c443601e54056884669d0dd001b5644bea0c5401ca03743905000dc61989603e0850183186ea602c181078844262bd401078844263617819688686e08618120b6088ed1410f211a1ea0d04f82b0d883004a28984e3705d200a80b,
0xb0cc402631d00162de6830d2f80104c5a557ef7c01ac498387e08501169e583e13f001520a86ae0bd0817609be0eca10019019422ec87801600b06a72a1101605b06a722010192c49557e09c018ac42ea3e201818e5a6e06c085010eb5983ec87801160c3dd8c8780110174550685f81b02d9551e84481a05986a72201011109ee46487d010e0c6c7ec86a81100f4550e85f8106a5e8d43c3d01b08868643c250182763ea362010180364dd05c0d812a360dd160aa81a8360dd164810148360d52412f812b520bae80af81560a0ea40c2201,
0xa8ca69d6222991b0d4831046178c04d998d23c85e1171316a62099cfb0d843322a2be16d8843322a1fe1055990a23e396170d741a222199906a442d23cbd6196d48310524f8c579080a32098efb09609104514f4823505d200bb0b65826aa232c48ba80a69d228d58c04d6c0a23e19b986764910504d8c8eb61910504dfc043705d222d9cb23996e0055235022f70590540b0c2351b0de0ffd0222f5cd10fd078270174552684480b0144552685480b0144552685780a81445d2685480459013b7f49881a8c813d628a981b0c845262a3901,
0x561a96a43c1181840912a43c3d0166b5c8343c3d01821a6aa40c23018209e8decd130182904025fe268182904027f3630180904025fe3801a4ac4025f07d01a4ec4027f05501578216a0484c81578216a048498104e705d1e856811798160a485181042f05d1e85c810581c32a486f81501b1326282a01b0d84026281501560b46262819810636c2943c3d01848868643c3d01a4d015b7f05201b009c626281501560a0ea608220196098aae08320116c0154ec838018c0920d7fda00128f648d05061011758153ed065019609251803c681,
0x501b4326361101764f117620bd0150cc457625c101059968a60ae001700b16a6289501500ac5563e2981640b12a628bd01a0d34091f60681a01f40a0b601818e8e6876cc78016c4f0687e09881839904a083c900234968ae40a89622f44390ea2882234258de13dd022348bbae00bd5110174552685f8011992e02685f8009806ea2685a8008db40d6360181b02618d631c101130a6e6623c101704b4326208501104dc5d625c101170b16a620c201361c1c363c850162416eae0085e650470350462c8cb04702d0454b544a446e40453d2b,
0x969c141e0d450108b5ce0ec84181480a08d7ef6a81179814a4105981a009b307e8150136cc15d6280501500a1dd6281901b02c1551f06981b035aa943c19818a086d140d3d01841916a43c1501820925d8c3c6818290402ecbe681a82e0dd1e48201760a08dec93201860920d7f07c01a40995d6282d81a40c6cd62efd01a474c826222d818688686633fc019288686633e101539844262bc1018a760830d2d801b0db00d0b40181ac4cb8a620af81578a10a6208981258a13a620ad018e4e69d620850186f64936208501b048ee26220101,
0xa84669d0454b0c96406b104d3a1b80a46cdec1f802b0da0960516b8c618086a1f6010d8ef486004a1b182b408eae02011b51588a50453b7c6e348dd0457b1b2b588baec2011bb0948d104517f4a8b48d104515fca8f48d1045153b2ab48d9160a8fc10948ba73c011410948e87fc011410548e87fc016410548bae0e416410548eae0e41640f5a18ded063026c5a0e47e085459247035053cc8c8e466e02a0851c8a45e977608afc96463950d14f822d0a6e60d04f822f5a0aded14108619880a13601616ac480ae80af9957408eae008a0f,
0x43993e0200ad0f4a8740a200ad70a0a668a20093f8658043a22a3d5f478010a23617ef538040522bc1eb64f70182221d9f2e4e6e0220851c0d991e022bde8f0b1b068220c56f521b06822bd16f961b028232692f520b06822bd16f900b02823e292f479a46022e0787928810a233f961929810a233f961978140a200902796c540a200a220968a08a200ba21539844222bc161b094402228d7f47190c42222196f479240222e07ef4789c0223607e1478840222bec61708f40d22df96196c629a0525d0c2ac46cd160adfcb0c44550e55782,
0x17108eae00b24fa0b48d91608a7c17888caa00a261a0344c90fe2002619080a320afda769c886ec55502769c88bec54782365c8d0045780c769c8d0e057d0228748d10517b0c80b4449ec1f802ac588b47e0851582dc818047d80c82b6391046edfc50d60910462f8c621f3107f5b8026ac65907e0ba3a04f7059226c53996dc1e0223c3ba6d981e0223c3cf4a1b02a228fd69b0ccb90620ab8f82826aa200bb0f538044222bc16b578040222a696b658a690620854bb02f0101e098b928760910dd2582625c5901e0b84a822f4111e0ad67,
0x04c302b7f40791969c350e03c802961e0aa0a0c88fb034cd504410d0a80e69d0c44b5006344ea8446d500475960164680cb0d440506454f044b41511646dfc04cab0aec4555f50544510646c8406744d98446b8c50144560647b7c8eb619904468fca0774230c463588eb442606452fca06740d04410dc828034dec3c802b0843251fc0802829c25aec0c8a5829044dec0c8af8088686e93c8f08c98186e13c8fa718206a04a08988a76099052c88c08360dd760c8e504da0e6ad148b26e741c3e44688c70d745106447a4a80c3511e456fc,
0x6ef4a0d05d30708a520ba600878a60530387e0878a60530387e2011f8ec46cd0456afc88c669d0dd0a82170a6e622241618398a0d04c1fc78251b5d1e0980a8251b5d1e19802b08628a12401708e75019044380c70534606e0878a0ec5e8ded14a822ec46d50456fcc8a181dd230ede10e341c923e3961900912a23cbd610835cdd23d01e41097402228dcf41097402228dff43192402222296f12d66c9223d9f8a00c45d0e457d8a0f410d16454f8a0b6499044617ca01740d0645f88a0f4459064553ba0a669d0c44b78560b4626289991,
0xa0744d9844410cb0984028c46ba29690457064622faccdb0d7e468a2a0f4c590c41082421f0687f5880286774200d0480283983221f608c707030683e208ef07026e476248bcb0246824fc08cc161e6d4e12c8022f916d1055086fb02c3831e468c6701b4034c468e35613451064520f046f2513e4453326f4c390c46b82440a82ae047d59501b432ac4516717426a7e12c80216820c5e93c80244125d17e4478344095d11e46f8da414cad07048886588c120d048828aae08a5e0bd106234483ec1f81160a70081fe16916ac568a57d0191,
0x0c8dbeae0c479113030681ec2f910cd2c031fe2891170b4626208991178a6826226911160e6a7632e99117803838d5af911084aeae0e411010560e47e0c88408360e66a0c8dc820a6aa608bb11861b42262a5511310b4626221911378016aac8851108364dd07048b8114a682e5048bc10c62b87e401200cf63a376447b6369c123ec4455b11882c2220dfe10d8990323487e1168c14d23cbd61114993a23cbd61110b06822c9d6f11826c622e016b1382683223c3eb1382682223e96b31826b32221beb171b068200a86f161e091ed14a82,
0xb01588a13c0191acd04317ea2a9104ed8517ee7a115198402ad048d2b0d300b1e0c8d486e669d0d0402106b4441e12c8fca08810a81e08d98e4e69d0d04882574046ae00c8c07659be0ec20111ac49b607e08511b04dc0d6f0488297006e4602c491860b422636179186e669d62219119298186633f911561a0ea608ba11b0086e06f21111266743d0d04882708f4076f048f26209baaec8b811604b0687e08511604b0387e08511a40a6aa632d491868868663e2791868868663e2491ac4cb8a620af91a01442a53e0191a01446a72a0191,
0x71808ea2a09bd096cc837623c13a378a1170d06d0213920481e1ef82b02e0d51e0a216311a0e60514b8ca845b5d1e5411710474550e55f8216ce6b7632c481160c3cd63e3901b01c9ad17040212192340083ef80b0943411fc0012b0c86d243c004cb01b0384c8403fb0189ad43c0053a0e443d0ea0012a0db41a0d60012a4f49a77704021234258de13dd0060430380c7ef80924700b683ef80b0470041e953809647035083e480b0470081e9da80b0470170c16500b0470351e7428092470170d3c280904701d0de0a80964701d0d24a80,
0x0a445e0ec3e7805644460cde2a0068456eac1c05800a446cbe93cd80684721a7ef4500684725d1e74580b0442b81f1ea80ac44684173ea807245a85e93c780b044bd50a225005644aea0c61480a84669d0c6ca00ac41b607e11500a0418687e1150096418aae013200644312a6213d00565e0e60d14d00969c6d0e02e000b0db01a0d420002f8a69d0d06b007245a8aecfd5006e4668b6a3fb008e445dd1f15a00484420d7f36a80b02f0071e84039b0442d51f1040076442c7ed14780ac442887f14780a84420d7b3d280a845c5d0a5c480,
0xb044ed50a22300884669d0c17a00a84435d1e153804c4435a1e17d006a44d940c7fa00964422ae182a00b0442881fc3000a0418687e18780b041c306e107802d9a4420d04f80a8466860a3c6800e446cdec16a80825cddd1e12d8088760960dd1b00375a1a7ed045000d9a0b6ad147808a4658d6d3ca8082433370d3d800a0a5e8d0fe2000a064edd0c5e000a01c8ad0a2ec8057408eae020c0009408ade0d2300319a0c60d14b8010462e87e1ca801045b5b7e543800e4658d7e17a001045e85ed91a8080246cdec1f80031026e40d2cb80,
0xa08340a8160010a01c6cd17e00108a820ba0c4801ba8f4c510d0001192d49510d3c011b0d43511e80010960f11d0d040d26c0f1077f040d206344dd85040d2561e0ea0a0c08b2b488dde412880a8160913e20c00b0d60911e18c0069986e0228c58097813aa2412801a8f60910c6ca00a8f420d228d280458025a234bd00b0908841f12b804d98884ac3d280a490884883e880b090884883e88097014600c6088043996e00451301423725d04493014198402a4be881a0374211760800829034dec3c800829035d1f188008e760990d14880,
0x10452e87fc30000c462e81e16f8028446dd8c12a8010466856ae230030466856a23b001045e856be33003045a85e93c50030442d78822a8010442c57fdb40012442cbe93c780084730d7f15b8008446cdeceda000845d8d7fd1a00084730d7ed5b800845e8d6be330008466e66a3ce8008446e66b3ee8010442eac1c1f8010452e0ece5d001646460ed99a0008456e0eda1d8010470687e9d280084700d7f35d8008470681e36f8010cdc5d0f0402131133600d3c021699868967040e5ac9810a813c0ca9088686ed000d7b0886868d040c2,
0xa4f4c0276228814d4835de43e8812b8108aa80af815680402e506481480b3217f59681965a0a00ce3a01acd10947e0aa8196d509472085018a350dd052ca818a820bb7e48201119a4200ee380196086a04f27801521906ae0be081500906ae1620818c090285fe2001760905180a3d0196190aae189201b02d0d51e0a201b0090d51e75581ac093507f1b801b0194504fc2401b009c504dc1b811680151e93e001168014aeda200116801648143d01b0820d5241220140ec1517ea7a01400a5a87f26881401a82a53e3801400a85d53c2d81,
0x25026e40d2c88043804024d3de814298402e93e381414036ae03ed0141404025fe380140ac4025ea7d01414835de43e881828238d0448d8182823aa0453d0196823aa04538018a820ad0448d8156820ea04522018a820ea0c62d0157810ea0452a014b810ea0c615018e9a6a0045200156098ea41c1a0196098aa41c3201b059c200dc20814e086a0cde2001480b0217f416811694121eca78019609221e03c68157810ea240aa01760b021a1e15014d88402a4be881768040281e1501a0804027f1a001a0804025fe2001a0ac4025fe2481,
0x718820d450488009886ca2704880704b4320d04880704b4620d048809611341e03c8809611141e03c880b0d8b106210780b04f00a229d480b0370422214980b0d0b10083e880b0122911f061806d8088d7e1680048f48d90c52880a8c669d0c6ca002ef720da010800ac1c6e0173c28016826c3e50480010174552645f80978042aa0451808a760ea36c8500a0764990c449005150451e846f80a83425d670558082e66856e3d800a074cd90c46100574046ae045180b08842d8446b80b0d82234c46880964f11d0c46880705b4620c46880,
0x96499510c45d00b0130381e99880a0c842d4446c80ac8820d8446f8048b4456ec45180406743d0c42b809611357803d80008c86d3633e68008c86d36336f809257031083ef8008c86d9633e68076c5b8dec16a80646f16a627c5008ece69d622028036570310d24c80b0c44550e55780705b4606e202808c193605fe0280a4c842d4446880311a0e60d1488042763e00d2c800a0c343a4160800821114dec3c880866743d0d04880420b027ade3501420b03d4de3501420b0684d3db81420b00d7e9e401420b05d1a3d3014209360ecbe681,
0x4209360ecfe681420a3e04cda50143986e0ad183014358ee0ec22301420a68d6dd130142f44024d93b0142093eae182d01420ac2ded83801420b43d4dc3101b085b021fc1281b085aba13c0101a009b585fe1301a4246db0f3e88182090687ea23818009028e0ffd0180090387ea3801860900d7f0548186090387f05501a0090285fe2101861906a72a2881820ab20ecbd68197006a0e181b01705b4200dc23810c85beae094781368416ae16050116cc3c7ec46880164c3dd8c46880374995d63c850016cdbcb633fb0008f608d61d1d80,]


class Block:
    def __init__(self, width=1, height=1, name=0):
        self.h = height
        self.w = width
        self.name = name


class Plate:
    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height
        self.plateArray = [['0'] * width for _ in range(height)]
        self._initPlate()

    def _initPlate(self):
        for i in range(self.height):
            for j in range(self.width):
                self.plateArray[i][j] = '0'

    def draw(self):
        line = ''
        for i in range(self.height):
            for j in range(self.width):
                line += self.plateArray[i][j] + ' '
            print(line)
            line = ''

    def putBlock(self, block, x=0, y=0, direction=0):
        h = [block.w, block.h][direction == 0]
        w = [block.h, block.w][direction == 0]
        n = block.name
        if h + y > self.height or w + x > self.width:
            # print('超边 放不下')
            return False

        if not self._isEmptySubBlock(x, y, w, h):
            # print('这区域里有别的东西，放不下')
            return False

        self._updateSubBlock(x, y, w, h, n)
        return True

    def _updateSubBlock(self, x=0, y=0, width=1, height=1, n='0'):
        for i in range(height):
            for j in range(width):
                self.plateArray[y + i][x + j] = n

    def _isEmptySubBlock(self, x=0, y=0, width=1, height=1):
        valueChecker = '0'
        for i in range(height):
            for j in range(width):
                currentPotValue = self.plateArray[y + i][x + j]
                if currentPotValue != '0':
                    valueChecker = currentPotValue

        return valueChecker == '0'

    def putBlocks(self, blocks):
        # 深度优先递归
        b = blocks[0]
        directions = ([0, 1], [0])[b.w == b.h]
        for i in range(self.height):
            for j in range(self.width):
                for dir in directions:
                    # 尝试在ji位置放置一块
                    if self.putBlock(b, j, i, dir):
                        currenBlockCount = len(blocks)
                        if currenBlockCount == 1:
                            # 放置成功后发现已经是最后一块了，
                            return True

                        remainingBlocks = blocks[1: currenBlockCount]
                        if self.putBlocks(remainingBlocks):
                            # 对剩下的块深度优先递归，看看是否成功
                            return True

                        # 剩下的块都递归完了，并未成功，则擦除当前块
                        self.erasureBlock(b, j, i, dir)

        # 所有位置都遍历了一遍还未成功，则此次递归失败
        return False

    def erasureBlock(self, block, x=0, y=0, direction=0):
        h = [block.w, block.h][direction == 0]
        w = [block.h, block.w][direction == 0]
        self._updateSubBlock(x, y, w, h, '0')
        
# 初始化拼图块
block_H = Block(3, 4, 'H')# 白 12
block_G = Block(2, 5, 'G')# 白 10
block_F = Block(3, 3, 'F')# 黄 9
block_E = Block(2, 4, 'E')# 红 8
block_D = Block(2, 3, 'D')# 红 6
block_C = Block(1, 5, 'C')# 白 5
block_B = Block(2, 2, 'B')# 白 4
block_A = Block(1, 4, 'A')# 红 4
block_1 = Block(1, 1, '1')# 蓝 1
block_2 = Block(1, 2, '2')# 蓝 2
block_3 = Block(1, 3, '3')# 蓝 3


def _decodeToPlate(targetPlate, code, keyBlocks, otherBlocks):
    tempCode = code
    keyBlocks.reverse()
    for e in keyBlocks:
        inf = 0xff & tempCode
        tempCode >>= 7
        x = (0b1110000 & inf) >> 4
        y = (0b1110 & inf) >> 1
        direction = 1 & inf
        targetPlate.putBlock(e, x, y, direction)
    keyBlocks.reverse()
    targetPlate.putBlocks(otherBlocks)


def decode(index, codeBignit):
    codeByteLength = 7
    moveStepCount = index * codeByteLength * 8
    decodeBlocks = [block_H, block_G, block_E,
                    block_D, block_C, block_A, block_3, block_2]
    opr = int('0x' + 'ff'*codeByteLength, 16) << moveStepCount
    code = (opr & codeBignit) >> moveStepCount
    newPlate = Plate(width=8, height=8)
    _decodeToPlate(newPlate, code, decodeBlocks, [block_F, block_B, block_1])
    return newPlate

force = ForceSensor('F')
hub = MSHub()
edge_brightness = 66

def show_left_edge():
    hub.light_matrix.set_pixel(0, 0, edge_brightness)
    hub.light_matrix.set_pixel(0, 1, edge_brightness)
    hub.light_matrix.set_pixel(0, 2, edge_brightness)
    hub.light_matrix.set_pixel(0, 3, edge_brightness)
    hub.light_matrix.set_pixel(0, 4, edge_brightness)


def show_right_edge():
    hub.light_matrix.set_pixel(4, 0, edge_brightness)
    hub.light_matrix.set_pixel(4, 1, edge_brightness)
    hub.light_matrix.set_pixel(4, 2, edge_brightness)
    hub.light_matrix.set_pixel(4, 3, edge_brightness)
    hub.light_matrix.set_pixel(4, 4, edge_brightness)


def show_top_edge():
    hub.light_matrix.set_pixel(0, 0, edge_brightness)
    hub.light_matrix.set_pixel(1, 0, edge_brightness)
    hub.light_matrix.set_pixel(2, 0, edge_brightness)
    hub.light_matrix.set_pixel(3, 0, edge_brightness)
    hub.light_matrix.set_pixel(4, 0, edge_brightness)


def show_bottom_edge():
    hub.light_matrix.set_pixel(0, 4, edge_brightness)
    hub.light_matrix.set_pixel(1, 4, edge_brightness)
    hub.light_matrix.set_pixel(2, 4, edge_brightness)
    hub.light_matrix.set_pixel(3, 4, edge_brightness)
    hub.light_matrix.set_pixel(4, 4, edge_brightness)


def set_pixels(stage, puzzle):
    light_x = 0
    light_y = 0
    puzzle_x = 0
    puzzle_y = 0
    if stage == 'LT':
        show_left_edge()
        show_top_edge()
        light_x = 1
        light_y = 1
        puzzle_x = 0
        puzzle_y = 0
    if stage == 'RT':
        show_right_edge()
        show_top_edge()
        light_x = 0
        light_y = 1
        puzzle_x = 4
        puzzle_y = 0
    if stage == 'LB':
        show_left_edge()
        show_bottom_edge()
        light_x = 1
        light_y = 0
        puzzle_x = 0
        puzzle_y = 4
    if stage == 'RB':
        show_right_edge()
        show_bottom_edge()
        light_x = 0
        light_y = 0
        puzzle_x = 4
        puzzle_y = 4
    for i in range(0, 4):
        for j in range(0, 4):
            if puzzle.plateArray[puzzle_y + j][puzzle_x + i] in ['1', '2', '3']:
                hub.light_matrix.set_pixel(light_x + i, light_y + j, 100)
            else:
                hub.light_matrix.set_pixel(light_x + i, light_y + j, 33)


stages = ['LT', 'RT', 'LB', 'RB']

currentScreen = 0
newQuestion = True
while True:
    wait_for_seconds(1)
    if force.is_pressed():
        hub.speaker.play_sound('1234')
        newQuestion = True
    if newQuestion:
        # 出题
        puzzles = a1[random.randint(0, 49)]
        puzzle = decode(random.randint(0, 24), puzzles)
        puzzle.draw()
        for i in range(0, 4):
            set_pixels(stages[i], puzzle)
            wait_for_seconds(1.5)
            hub.light_matrix.off()
        set_pixels(stages[0], puzzle)
        hub.speaker.play_sound('Tadaa', 50)
        currentScreen = 0
        newQuestion = False
    if hub.right_button.was_pressed():
        hub.speaker.beep()
        currentScreen += 1
        if currentScreen == 4:
            currentScreen = 0
        hub.light_matrix.off()
        set_pixels(stages[currentScreen], puzzle)
    if hub.left_button.was_pressed():
        hub.speaker.beep()
        currentScreen -= 1
        if currentScreen == -1:
            currentScreen = 3
        hub.light_matrix.off()
        set_pixels(stages[currentScreen], puzzle)
