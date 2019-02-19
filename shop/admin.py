from django.contrib import admin
from .models import Shop, Item


@admin.register(Shop)  # 장식자 (Decorators)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'created_at']


@admin.register(Item)  # 장식자 (Decorators)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_public', 'created_at']



# @admin.register(Shop)
# class ShopAdmin(admin.ModelAdmin):
#    list_display = ['name', 'desc', 'address'] #게시판 항목 수정
#    list_display_links = ['name'] #title 부분에 링크를 걸 수 있도록. 이거 안해주면 디폴트는 첫번째 컬럼이 링크(id)
#    list_filter = ['name']
#    search_fields = ['name'] #타이틀을 검색할 수 있도록 검색필드 추가

#    def short_content(self, desc):
#        return name.content[:20] + ' ...'

# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#    pass