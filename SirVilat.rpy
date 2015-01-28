﻿init:
    $ sm = Character(u'Семпай', color="#920000", what_color="E2C555", drop_shadow = [ (-1, -1), (1, -1), (-1, -1), (1, -1) ], drop_shadow_color = "#000")
    $ li = Character(u'Лиза', color="#920000", what_color="E2C555", drop_shadow = [ (-1, -1), (1, -1), (-1, -1), (1, -1) ], drop_shadow_color = "#000")
    $ mods["SirVilat"] = u"Бесконечный Холод"
    
    image bg home = "mods/SirVilat/image/room_1.jpg"
   #  image ss_li = "mods/sirvilat/image/sprites/lisa.png"
 
label SirVilat:
    $ prolog_time()
    $ persistent.sprite_time = "day"
 
    # {w}text   -слово текст еапичатается не сразу  
    # {i}{/i} -курсив
 
# Дописал холод и лег спать
    play music  music_list["sunny_day"] fadein 1
    scene bg semen_room
    "Я дописал очередной черновик следующей серии Холода, который наврняка будет еще много раз переписан и в итоге от проделанной работы не останется и следа"
    "На часах светилось 6:21 утра"
    th "Наверное, пора уже и спать ложиться. К черту этот Холод, к черту Лизу эту проклятую - я все равно как был форевеалоуном, так и останусь"
    "Можно было еще пройти какой-нибдуь рут из мода для Бесконечного Лета напоследок, но и его я послал к черту"
    th "И без Лета хоть вскрывайся {i} - думал я, брякнувшись в кровать.{/i}"
    "Сон долго не шел, я ворочался с бока на бок, а мысли скакали с одного на другое, ни на чем толком не сосредотачиваясь"
    "размытые образы новых сцен Холода мутно плавали перед глазами, мелькала Лиза в разных эпизодах, обличиях"
    "Я наконец-то заснул."
    
    
# Прибытие (Сплэш монитора с фразой "прибытие"

# Очнулся в автобусе
    play music  music_list["door_to_nightmare"] fadein 1
    show unblink
    scene bg int_bus 
    with dissolve2 
    "Еще не открыв глаза я уже почуял неладное - тело затекло в сидячей позе"
    th "Ну не в новом же кресле я вчера уснул - мелькнула мысль"
    "Все быстро стало ясно, а точнее нифига не ясно - я сидел в автобусе, чей номер молниеностно всплыл в памяти. Я вроде не Семен, так какого хера я тут очутился?"
    sm "Ну ахереть теперь"
    "Только и сказал я."
    th "Нет, я конечно мечтал попасть на месте дауна-Семена, но как-то не особо был к этому готов. С другой стороны, это место было мне как родное и вряд ли чем-то удивит, да и бояться нечего"

# Вырубить музыку
    stop music fadeout 3
# Вышел, увидел Семена   
    scene bg ext_bus 
    with dissolve2
    "Оказавшись на свежем водухе под палящим солнцем я тут же увидел и главного героя всей истории - Семена. Он валялся на асфальте и отвратительно ревел навзрыд" 
    play ambience sfx_lena_hits_alisa 
    with vpunch
    stop ambience
    "Без лишних раздумий я смачно пнул ДЦПщника по хребту и отскочил за один из постоментов"
    scene cg d6_pioneer
    th "Эх, надо было пнуть дважды - все равно он бы не успел заметить"

# Лиза пришла    Треш коммит
    scene ext_camp_entrance_day 
    show li normal casual at right
    li "Ну ты герой пиздец"
<<<<<<< HEAD
    я "ну нехер разлёживаться утром"
    ли "а если бы ты ему ребро или позвоночник сломал"
    я "Ну давай проверим"
    "Тем временем Семёшка уже тихо сбегал отсюда"
    я"Остановись идиот"
    "Он не послушал и бежал постоянно оглядываясь"
    "Зря.Он благополучно споткнулся о камень и влетел головой в рядом стоящее дерево"
=======
    return
>>>>>>> origin/master
        
