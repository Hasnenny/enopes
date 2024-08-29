from pyrogram.enums import ChatMembersFilter, ChatMemberStatus, ChatType
from database import get_db_constractors, get_db_manager, get_db_admin, get_db_special, get_db_general_rtb
from config import sudoers, developer


def sudo(m):
    leader = False
    try:
        for per in sudoers:
            if m.from_user.id == per:
                leader = True
    except Exception as e:
        print("sudo " + str(e))

    return leader


def secsudo(m):
    leader = False
    lang = get_db_general_rtb("secdeveloper")
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[0]:
                    leader = True
        except Exception as e:
            print("genspecial " + str(e))
    if leader or sudo(m):
        leader = True
    else:
        leader = False
    return leader


def sudo2(m):
    leader = False
    if developer is None:
        leader = False
    else:
        try:
            for per in developer:
                if m.from_user.id == per:
                    leader = True
        except Exception as e:
            print("sudo2 " + str(e))

    if leader or sudo(m) or secsudo(m):
        leader = True
    else:
        leader = False
    return leader


def genspecial(m):
    leader = False
    lang = get_db_general_rtb("genspecial")
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[0]:
                    leader = True
        except Exception as e:
            print("genspecial " + str(e))

    return leader


def manager(m):
    leader = False
    lang = get_db_manager(m.chat.id)
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[1]:
                    leader = True
        except Exception as e:
            print("manager " + str(e))
    if leader or sudo(m) or secsudo(m) or sudo2(m):
        leader = True
    else:
        leader = False
    return leader


def constractors(m):
    leader = False
    lang = get_db_constractors(m.chat.id)
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[1]:
                    leader = True
        except Exception as e:
            print("constractors " + str(e))
    if leader or sudo(m) or secsudo(m) or sudo2(m) or manager(m):
        leader = True
    else:
        leader = False
    return leader


def admin(m):
    leader = False
    lang = get_db_admin(m.chat.id)
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[1]:
                    leader = True
        except Exception as e:
            print("admin " + str(e))
    if leader or sudo(m) or secsudo(m) or sudo2(m) or manager(m) or constractors(m):
        leader = True
    else:
        leader = False
    return leader


def adminCB(m):
    leader = False
    lang = get_db_admin(m.message.chat.id)
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[1]:
                    leader = True
        except Exception as e:
            print("admin " + str(e))
    if leader or sudoCB(m) or secsudoCB(m) or sudo2CB(m) or managerCB(m) or constractorsCB(m):
        leader = True
    else:
        leader = False
    return leader

def sudoCB(m):
    leader = False
    try:
        for per in sudoers:
            if m.from_user.id == per:
                leader = True
    except Exception as e:
        print("sudo " + str(e))
    return leader


def secsudoCB(m):
    leader = False
    lang = get_db_general_rtb("secdeveloper")
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[0]:
                    leader = True
        except Exception as e:
            print("genspecial " + str(e))
    if leader or sudoCB(m):
        leader = True
    else:
        leader = False
    return leader


def sudo2CB(m):
    leader = False
    if developer is None:
        leader = False
    else:
        try:
            for per in developer:
                if m.from_user.id == per:
                    leader = True
        except Exception as e:
            print("sudo2 " + str(e))

    if leader or sudoCB(m) or secsudoCB(m):
        leader = True
    else:
        leader = False
    return leader

def managerCB(m):
    leader = False
    lang = get_db_manager(m.message.chat.id)
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[1]:
                    leader = True
        except Exception as e:
            print("manager " + str(e))
    if leader or sudoCB(m) or secsudoCB(m) or sudo2CB(m):
        leader = True
    else:
        leader = False
    return leader


def constractorsCB(m):
    leader = False
    lang = get_db_constractors(m.message.chat.id)
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[1]:
                    leader = True
        except Exception as e:
            print("constractors " + str(e))
    if leader or sudoCB(m) or secsudoCB(m) or sudo2CB(m) or managerCB(m):
        leader = True
    else:
        leader = False
    return leader

def special(m):
    leader = False
    lang = get_db_special(m.chat.id)
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[1]:
                    leader = True
        except Exception as e:
            print("special " + str(e))
    if leader or sudo(m) or secsudo(m) or sudo2(m) or manager(m) or constractors(m) or admin(m):
        leader = True
    else:
        leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def get_Rank(m):
    leader = "عضو"
    if m.from_user.id == 7031471363:
        leader = "مطور السورس"
    else:
        if m.from_user.id == 7031471363:
            leader = "مبرمج السورس"
        else:
            if sudo(m):
                leader = "مطور اساسي"
            else:
                if secsudo(m):
                    leader = "مطور ثانوي"
                else:
                    if sudo2(m):
                        leader = "مطور"
                    else:
                        if genspecial(m):
                            leader = "مميز عام"
                        else:
                            if manager(m):
                                leader = "مالك"
                            else:
                                if constractors(m):
                                    leader = "منشئ"
                                else:
                                    if admin(m):
                                        leader = "ادمن"
                                    else:
                                        if special(m):
                                            leader = "مميز"

    return leader


########################################################################################################################
########################################################################################################################

def sudooo(u):
    leader = False
    for per in sudoers:
        if u == per:
            leader = True
    return leader


def secsudooo(u):
    leader = False
    lang = get_db_general_rtb("secdeveloper")
    if lang is None:
        leader = False
    else:
        for per in lang:
            if u == per[0]:
                leader = True
    if leader or sudooo(u):
        leader = True
    else:
        leader = False
    return leader


def sudooo2(u):
    leader = False
    if developer is None:
        leader = False
    else:
        for per in developer:
            if u == per:
                leader = True
    if leader or sudooo(u) or secsudooo(u):
        leader = True
    else:
        leader = False
    return leader


def genspecialll(u):
    leader = False
    lang = get_db_general_rtb("genspecial")
    if lang is None:
        leader = False
    else:
        for per in lang:
            if u == per[0]:
                leader = True
    return leader


def managerrr(u, m):
    leader = False
    lang = get_db_manager(m.chat.id)
    if lang is None:
        leader = False
    else:
        for per in lang:
            if u == per[1]:
                leader = True
    if leader or sudooo(u) or secsudooo(u) or sudooo2(u):
        leader = True
    else:
        leader = False
    return leader


def constractorsss(u, m):
    leader = False
    lang = get_db_constractors(m.chat.id)
    if lang is None:
        leader = False
    else:
        for per in lang:
            if u == per[1]:
                leader = True
    if leader or sudooo(u) or secsudooo(u) or sudooo2(u) or managerrr(u, m):
        leader = True
    else:
        leader = False
    return leader


def adminnn(u, m):
    leader = False
    lang = get_db_admin(m.chat.id)
    if lang is None:
        leader = False
    else:
        for per in lang:
            if u == per[1]:
                leader = True
    if leader or sudooo(u) or secsudooo(u) or sudooo2(u) or managerrr(u, m) or constractorsss(u, m):
        leader = True
    else:
        leader = False
    return leader


def specialll(u, m):
    leader = False
    lang = get_db_special(m.chat.id)
    if lang is None:
        leader = False
    else:
        for per in lang:
            if u == per[1]:
                leader = True
    if leader or sudooo(u) or secsudooo(u) or sudooo2(u) or managerrr(u, m) or constractorsss(u, m) or adminnn(u, m):
        leader = True
    else:
        leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def get_Rankkk(u, m):
    leader = "عضو"
    if u == 7031471363:
        leader = "مطور السورس"
    else:
        if u == 7031471363:
            leader = "مبرمج السورس"
        else:
            if sudooo(u):
                leader = "مطور اساسي"
            else:
                if secsudooo(u):
                    leader = "مطور ثانوي"
                else:
                    if sudooo2(u):
                        leader = "مطور"
                    else:
                        if genspecialll(u):
                            leader = "مميز عام"
                        else:
                            if managerrr(u, m):
                                leader = "مالك"
                            else:
                                if constractorsss(u, m):
                                    leader = "منشئ"
                                else:
                                    if adminnn(u, m):
                                        leader = "ادمن"
                                    else:
                                        if specialll(u, m):
                                            leader = "مميز"

    return leader


########################################################################################################################
########################################################################################################################

async def get_Rank_ana_meen(m):
    leader = "↯︙شتريد من البوت"
    if m.from_user.id == 7031471363:
        leader = "↯︙ها يعيون ديفد"
    else:
        if m.from_user.id == 7031471363:
            leader = "↯︙راح اغير اسمي ياخي"
        else:
            if sudo(m):
                leader = "نعم اخي"
            else:
                if secsudo(m):
                    leader = "!!!!!!!"
                else:
                    if sudo2(m):
                        leader = "هلا يعيوني"
                    else:
                        if genspecialll(m):
                            leader = "تفضلل !!!!"
                        else:
                            if manager(m):
                                leader = "شتريد اخيي"
                            else:
                                if constractors(m):
                                    leader = "!!!!!"
                                else:
                                    if admin(m):
                                        leader = "↯︙راح اغير اسمي ياخي"
                                    else:
                                        if special(m):
                                            leader = "نعمم"

    return leader


########################################################################################################################
########################################################################################################################

async def get_available_creator(c, m):
    creatorcheck = False
    creatorname = "لايوجد"
    creatorid = 0
    async for creator in c.get_chat_members(m.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        if creator.status == ChatMemberStatus.OWNER:
            creatorname = creator.user.first_name
            creatorid = creator.user.id
            if m.from_user.id == creator.user.id:
                creatorcheck = True

    return creatorcheck, creatorname, creatorid


async def get_Rank_ana_feen(m, c):
    if m.chat.type == ChatType.PRIVATE:
        leader = "هلا اعيوني"
    else:
        checkcreator = await get_available_creator(c, m)
        if checkcreator[0]:
            leader = "تفضل اخي"
        else:
            leader = f"هلا اخي [{checkcreator[1]}](tg://user?id={checkcreator[2]})"
    return leader

########################################################################################################################
########################################################################################################################
