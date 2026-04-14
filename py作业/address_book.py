import json
import os

# 全局变量
ADDRESS_BOOK_FILE = "address_book.json"
PASSWORD_FILE = "password.json"
address_book = {}


def load_address_book():
    """加载通讯录数据"""
    global address_book
    if os.path.exists(ADDRESS_BOOK_FILE):
        with open(ADDRESS_BOOK_FILE, 'r', encoding='utf-8') as f:
            address_book = json.load(f)
    else:
        address_book = {}


def save_address_book():
    """保存通讯录数据"""
    with open(ADDRESS_BOOK_FILE, 'w', encoding='utf-8') as f:
        json.dump(address_book, f, ensure_ascii=False, indent=2)


def setup_password():
    """设置或验证密码"""
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r', encoding='utf-8') as f:
            stored_password = json.load(f)
        
        attempts = 3
        while attempts > 0:
            password = input("请输入密码：")
            if password == stored_password:
                return True
            else:
                attempts -= 1
                print(f"密码错误，还有 {attempts} 次机会")
        return False
    else:
        # 首次运行，设置密码
        password = input("请设置登录密码：")
        with open(PASSWORD_FILE, 'w', encoding='utf-8') as f:
            json.dump(password, f)
        print("密码设置成功！")
        return True


def add_contact():
    """添加或修改联系人"""
    name = input("请输入联系人姓名：").strip()
    phone = input("请输入联系电话：").strip()
    email = input("请输入电子邮箱：").strip()
    
    if name in address_book:
        print(f"联系人 {name} 已存在，当前信息：")
        print(f"电话：{address_book[name]['phone']}")
        print(f"邮箱：{address_book[name]['email']}")
        
        choice = input("是否修改该联系人信息？(y/n)：").lower().strip()
        if choice == 'y':
            address_book[name] = {"phone": phone, "email": email}
            save_address_book()
            print("联系人信息已更新")
    else:
        address_book[name] = {"phone": phone, "email": email}
        save_address_book()
        print("联系人添加成功")


def search_contact():
    """查询联系人"""
    name = input("请输入要查询的联系人姓名：").strip()
    if name in address_book:
        print(f"联系人 {name} 的信息：")
        print(f"电话：{address_book[name]['phone']}")
        print(f"邮箱：{address_book[name]['email']}")
    else:
        print(f"联系人 {name} 不存在")


def show_all_contacts():
    """显示所有联系人"""
    if not address_book:
        print("通讯录为空")
    else:
        print("\n所有联系人信息：")
        print("-" * 50)
        for name, info in address_book.items():
            print(f"姓名：{name}")
            print(f"电话：{info['phone']}")
            print(f"邮箱：{info['email']}")
            print("-" * 50)


def delete_contact():
    """删除联系人"""
    name = input("请输入要删除的联系人姓名：").strip()
    if name in address_book:
        del address_book[name]
        save_address_book()
        print(f"联系人 {name} 已删除")
    else:
        print(f"联系人 {name} 不存在")


def add_initial_contacts():
    """添加初始的30条联系人信息"""
    initial_contacts = [
        {"name": "张三", "phone": "13800138001", "email": "zhangsan@example.com"},
        {"name": "李四", "phone": "13800138002", "email": "lisi@example.com"},
        {"name": "王五", "phone": "13800138003", "email": "wangwu@example.com"},
        {"name": "赵六", "phone": "13800138004", "email": "zhaoliu@example.com"},
        {"name": "孙七", "phone": "13800138005", "email": "sunqi@example.com"},
        {"name": "周八", "phone": "13800138006", "email": "zhouba@example.com"},
        {"name": "吴九", "phone": "13800138007", "email": "wuju@example.com"},
        {"name": "郑十", "phone": "13800138008", "email": "zhengshi@example.com"},
        {"name": "钱一", "phone": "13800138009", "email": "qianyi@example.com"},
        {"name": "孙二", "phone": "13800138010", "email": "suner@example.com"},
        {"name": "周三", "phone": "13800138011", "email": "zhousan@example.com"},
        {"name": "吴四", "phone": "13800138012", "email": "wusi@example.com"},
        {"name": "郑五", "phone": "13800138013", "email": "zhengwu@example.com"},
        {"name": "王六", "phone": "13800138014", "email": "wangliu@example.com"},
        {"name": "赵七", "phone": "13800138015", "email": "zhaoqi@example.com"},
        {"name": "孙八", "phone": "13800138016", "email": "sunba@example.com"},
        {"name": "周九", "phone": "13800138017", "email": "zhoujiu@example.com"},
        {"name": "吴十", "phone": "13800138018", "email": "wushi@example.com"},
        {"name": "郑一", "phone": "13800138019", "email": "zhengyi@example.com"},
        {"name": "钱二", "phone": "13800138020", "email": "qianer@example.com"},
        {"name": "孙三", "phone": "13800138021", "email": "sunsan@example.com"},
        {"name": "周四", "phone": "13800138022", "email": "zhousi@example.com"},
        {"name": "吴五", "phone": "13800138023", "email": "wuwu@example.com"},
        {"name": "郑六", "phone": "13800138024", "email": "zhengliu@example.com"},
        {"name": "王七", "phone": "13800138025", "email": "wangqi@example.com"},
        {"name": "赵八", "phone": "13800138026", "email": "zhaoba@example.com"},
        {"name": "孙九", "phone": "13800138027", "email": "sunjiu@example.com"},
        {"name": "周十", "phone": "13800138028", "email": "zhoushi@example.com"},
        {"name": "吴一", "phone": "13800138029", "email": "wuyi@example.com"},
        {"name": "郑二", "phone": "13800138030", "email": "zheng'er@example.com"}
    ]
    
    for contact in initial_contacts:
        address_book[contact["name"]] = {
            "phone": contact["phone"],
            "email": contact["email"]
        }
    save_address_book()
    print("已添加30条初始联系人信息")


def main():
    """主函数"""
    # 加载通讯录数据
    load_address_book()
    
    # 密码验证
    if not setup_password():
        print("密码错误，程序退出")
        return
    
    # 首次运行添加初始联系人
    if not address_book:
        add_initial_contacts()
    
    while True:
        print("\n=== 通讯录管理系统 ===")
        print("1. 添加/修改联系人")
        print("2. 查询联系人")
        print("3. 显示所有联系人")
        print("4. 删除联系人")
        print("5. 退出系统")
        
        choice = input("请选择操作 (1-5): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            show_all_contacts()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("再见！")
            break
        else:
            print("无效选择，请重新输入")


if __name__ == "__main__":
    main()
