import requests, random, urllib.parse

surname = ["an", "anh", "ao", "au", "ba", "bac", "bach", "ban", "bang", "banh", "bao", "be", "bi", "bien", "binh", "bo", "bui", "ca", "cai", "cam", "can", "canh", "cao", "cap", "cat", "chau", "che", "chiem", "chrieng", "chu", "chung", "chuong", "co", "cong", "cu", "cung", "da", "dai", "dam", "dan", "dang", "danh", "dao", "dau", "deo", "diem", "dien", "diep", "dieu", "dinh", "do", "doan", "doi", "don", "dong", "du", "duc", "duong", "duy", "gia", "giang", "giao", "giap", "ha", "han", "hau", "he", "hi", "hinh", "ho", "hoa", "hoang", "hong", "hua", "hung", "huong", "huynh", "kha", "khai", "khau", "khieu", "khoa", "khong", "khu", "khuat", "khuc", "khuong", "kieu", "kim", "kong", "la", "lac", "lai", "lam", "lang", "lanh", "le", "leng", "leu", "lien", "lieu", "linh", "lo", "lu", "luc", "luong", "luu", "luyen", "ly", "lyly", "ma", "mac", "mach", "mai", "man", "mang", "manh", "mau", "moc", "mua", "muc", "ngac", "ngan", "nghi", "nghiem", "ngo", "ngoc", "ngu", "nguy", "nguyen", "nham", "nhan", "nhu", "ninh", "nong", "ong", "pham", "phan", "phi", "pho", "phu", "phung", "phuong", "quach", "quan", "quang", "sai", "sam", "son", "su", "sung", "ta", "tan", "tang", "tao", "te", "thach", "thai", "tham", "than", "thang", "thanh", "thao", "thap", "that", "the", "thi", "thieu", "thinh", "thoa", "thoi", "thuc", "tiep", "tieu", "tinh", "to", "ton", "tong", "tra", "trac", "tran", "trang", "tri", "trieu", "trinh", "trung", "truong", "tu", "tuan", "ty", "ung", "uong", "van", "vi", "viem", "vien", "vo", "vu", "vuong", "vuu", "xa", "xung", "yen"]

middlename = ["cam", "chau", "dai", "dieu", "dinh", "duc", "hanh", "hoang", "hong", "minh", "thi", "thu", "van", "xuan"]

name = ["aaron", "abigail", "adam", "ai", "alan", "albert", "alexander", "alexis", "alice", "amanda", "amber", "amy", "an", "andrea", "andrew", "angela", "anh", "ann", "anna", "anthony", "arthur", "ashley", "austin", "bach", "barbara", "benjamin", "betty", "beverly", "bich", "billy", "bo", "bobby", "boi", "brandon", "brenda", "brian", "brittany", "bruce", "bryan", "carl", "carol", "carolyn", "catherine", "charles", "charlotte", "chau", "cheryl", "chi", "chien", "chloe", "christian", "christina", "christine", "christopher", "chuc", "chung", "claire", "cuc", "cynthia", "daniel", "danielle", "dat", "david", "deborah", "debra", "denise", "dennis", "di", "diana", "diane", "diep", "donald", "donna", "doris", "dorothy", "douglas", "duc", "dung", "duong", "duy", "dylan", "edward", "elijah", "elizabeth", "emily", "emma", "eric", "ethan", "eugene", "evelyn", "frances", "frank", "gabriel", "gary", "george", "gerald", "giang", "gloria", "grace", "gregory", "h", "ha", "han", "hang", "hanh", "hannah", "hao", "harold", "hau", "heather", "helen", "henry", "hien", "hiep", "hoa", "huan", "hue", "hung", "huong", "huy", "huyen", "huynh", "isabella", "jack", "jacob", "jacqueline", "jade", "james", "janet", "janice", "jason", "jean", "jeffrey", "jennifer", "jeremy", "jerry", "jesse", "jessica", "joan", "joe", "john", "johnny", "jonathan", "jordan", "jose", "joseph", "joshua", "joy", "joyce", "juan", "judith", "judy", "julia", "julie", "justin", "karen", "kate", "katherine", "kathleen", "kathryn", "kayla", "keith", "kelly", "ken", "kenneth", "kevin", "khai", "khang", "khanh", "khiem", "khuong", "khuyen", "kim", "kimberly", "kyle", "lam", "lan", "larry", "laura", "lauren", "lawrence", "le", "leah", "linda", "linh", "lisa", "liz", "loan", "loc", "logan", "loi", "long", "louis", "luan", "luong", "ly", "lynn", "m", "madison", "mai", "man", "margaret", "maria", "marie", "marilyn", "mark", "martha", "mary", "matthew", "megan", "melissa", "michael", "michelle", "minh", "moon", "nam", "nancy", "natalie", "nathan", "nga", "ngoc", "nha", "nham", "nhan", "nhi", "nhu", "nhung", "ni", "nicholas", "nicole", "ninh", "noah", "nuong", "oanh", "olivia", "pamela", "patricia", "patrick", "paul", "peter", "philip", "phong", "phung", "phuong", "quang", "quyen", "rachel", "ralph", "randy", "raymond", "rebecca", "richard", "robert", "roger", "ronald", "rose", "roy", "russell", "ruth", "ryan", "sam", "samantha", "samuel", "sandra", "sara", "sarah", "scott", "sean", "sen", "sharon", "shin", "shirley", "sky", "son", "sophia", "stephanie", "stephen", "steven", "susan", "t", "tam", "tan", "teresa", "terry", "thang", "thanh", "thao", "theresa", "thi", "thoa", "thomas", "thu", "thuan", "thuong", "thuy", "thuyen", "thy", "tien", "timothy", "toan", "tran", "trang", "trinh", "truc", "trung", "tuan", "tung", "tuyen", "tuyet", "tyler", "v", "van", "victoria", "vien", "vincent", "vinh", "virginia", "vuong", "vy", "walter", "wayne", "william", "willie", "y", "yen", "yui", "zachary", "zoe", "zoey"]

unique = ['**', '!', '@1', '213##', '#', '*', '&&', '&', '$', '!@#', '']
domain = ["gmail.com", "yahoo.com", "outlook.com", "ilamail.edu.vn"]

def generate_user():
	sname = random.choice(surname)
	mname = ""
	if(random.randrange(2) == 1):
		mname = random.choice(middlename)
	fname = random.choice(name)
	email = ""
	if(mname == ""):
		email = fname + sname + str(random.randint(1000, 9999)) + "@" + random.choice(domain)
	else:
		email = sname + mname + fname + str(random.randint(1000, 9999)) + "@" + random.choice(domain)
	password = sname + fname + str(random.randint(1000, 9999)) + random.choice(unique)

	return [email, password]

def generate_payload():
	email, password = generate_user()
	return f'email={urllib.parse.quote_plus(email)}&pass={urllib.parse.quote_plus(password)}&login='



url = "<PHISHING-FORM-URL>"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

for i in range(100000000):
	payload = generate_payload()
	response = requests.request("POST", url, data=payload, headers=headers, allow_redirects=False)
	if response.status_code != 302:
		print("Error")
		break
	if (i+1) % 600 == 0:
		print(i+1)
