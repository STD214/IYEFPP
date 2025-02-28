import requests
from datetime import datetime, timedelta

class PostManager:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        
    def get_all_posts(self):
        """Tüm gönderileri getir"""
        response = requests.get(f"{self.base_url}/posts")
        return response.json()
    
    def create_post(self, title, body, user_id):
        """Yeni gönderi oluştur"""
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = requests.post(f"{self.base_url}/posts", json=data)
        return response.json()
    
    def update_post(self, post_id, title, body):
        """Gönderi güncelle"""
        data = {
            "title": title,
            "body": body
        }
        response = requests.put(f"{self.base_url}/posts/{post_id}", json=data)
        return response.json()
    
    def delete_post(self, post_id):
        """Gönderi sil"""
        response = requests.delete(f"{self.base_url}/posts/{post_id}")
        return response.status_code == 200
    
    def search_by_user(self, user_id):
        """Kullanıcıya göre gönderileri ara"""
        response = requests.get(f"{self.base_url}/posts", params={"userId": user_id})
        return response.json()
    
    def search_by_title(self, keyword):
        """Başlığa göre gönderileri ara"""
        all_posts = self.get_all_posts()
        return [post for post in all_posts if keyword.lower() in post["title"].lower()]

# Kullanım örneği
def main():
    post_manager = PostManager()
    
    # Tüm gönderileri listele
    print("Tüm Gönderiler:")
    posts = post_manager.get_all_posts()
    print(f"Toplam {len(posts)} gönderi bulundu.")
    
    # Yeni gönderi oluştur
    print("\nYeni Gönderi Oluşturuluyor...")
    new_post = post_manager.create_post(
        "Yeni Gönderi",
        "Bu bir test gönderisidir.",
        1
    )
    print(f"Yeni gönderi oluşturuldu: {new_post}")
    
    # Gönderi güncelle
    print("\nGönderi Güncelleniyor...")
    updated_post = post_manager.update_post(
        1,
        "Güncellenmiş Başlık",
        "Güncellenmiş içerik"
    )
    print(f"Gönderi güncellendi: {updated_post}")
    
    # Kullanıcıya göre ara
    print("\nKullanıcı 1'in gönderileri:")
    user_posts = post_manager.search_by_user(1)
    print(f"Kullanıcı 1'e ait {len(user_posts)} gönderi bulundu.")
    
    # Başlığa göre ara
    print("\nBaşlıkta 'sunt' içeren gönderiler:")
    title_posts = post_manager.search_by_title("sunt")
    print(f"'{len(title_posts)}' gönderi bulundu.")
    
    # Gönderi sil
    print("\nGönderi Siliniyor...")
    if post_manager.delete_post(1):
        print("Gönderi başarıyla silindi.")
    else:
        print("Gönderi silinirken bir hata oluştu.")

if __name__ == "__main__":
    main()