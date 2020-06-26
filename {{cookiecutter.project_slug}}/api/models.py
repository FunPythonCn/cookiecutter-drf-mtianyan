# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MmallCart(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    checked = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mmall_cart'


class MmallCategory(models.Model):
    parent_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mmall_category'


class MmallOrder(models.Model):
    order_no = models.BigIntegerField(unique=True, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    shipping_id = models.IntegerField(blank=True, null=True)
    payment = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    postage = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    payment_time = models.DateTimeField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    close_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mmall_order'


class MmallOrderItem(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    order_no = models.BigIntegerField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_image = models.CharField(max_length=500, blank=True, null=True)
    current_unit_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mmall_order_item'


class MmallPayInfo(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    order_no = models.BigIntegerField(blank=True, null=True)
    pay_platform = models.IntegerField(blank=True, null=True)
    platform_number = models.CharField(max_length=200, blank=True, null=True)
    platform_status = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mmall_pay_info'


class MmallProduct(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    main_image = models.CharField(max_length=500, blank=True, null=True)
    sub_images = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mmall_product'


class MmallShipping(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    receiver_name = models.CharField(max_length=20, blank=True, null=True)
    receiver_phone = models.CharField(max_length=20, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=20, blank=True, null=True)
    receiver_province = models.CharField(max_length=20, blank=True, null=True)
    receiver_city = models.CharField(max_length=20, blank=True, null=True)
    receiver_district = models.CharField(max_length=20, blank=True, null=True)
    receiver_address = models.CharField(max_length=200, blank=True, null=True)
    receiver_zip = models.CharField(max_length=6, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mmall_shipping'


class MmallUser(models.Model):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    question = models.CharField(max_length=100, blank=True, null=True)
    answer = models.CharField(max_length=100, blank=True, null=True)
    role = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mmall_user'
