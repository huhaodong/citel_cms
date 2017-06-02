# 1. citel_cms

---

## 1.1. 目录

<!-- TOC -->

- [1. citel_cms](#1-citel_cms)
    - [1.1. 目录](#11-目录)
    - [1.2. 文档说明](#12-文档说明)
        - [1.2.1. 文档用途](#121-文档用途)
    - [1.3. 数据库设计](#13-数据库设计)
        - [1.3.1. cmsModel_items](#131-cmsmodel_items)
            - [1.3.1.1. 数据表描述](#1311-数据表描述)
            - [1.3.1.2. 数据表结构说明](#1312-数据表结构说明)
        - [1.3.2. cmsModel_user_account](#132-cmsmodel_user_account)
            - [1.3.2.1. 数据表描述](#1321-数据表描述)
            - [1.3.2.2. 数据表结构说明](#1322-数据表结构说明)
        - [1.3.3. cmsModel_admin_account](#133-cmsmodel_admin_account)
            - [1.3.3.1. 数据表描述](#1331-数据表描述)
            - [1.3.3.2. 数据表结构说明](#1332-数据表结构说明)

<!-- /TOC -->

---

## 1.2. 文档说明

---

### 1.2.1. 文档用途

该文档用于说明系统结构。

---

## 1.3. 数据库设计

### 1.3.1. cmsModel_items

#### 1.3.1.1. 数据表描述

该数据表用于保存文章信息，包含创建时间，栏目，文章名，内容链接。

#### 1.3.1.2. 数据表结构说明

|表项|数据类型|是否是主键|描述|注释|
|:---:|:---:|:---:|:---:|:---:|
|id|int auto_increment|是|用于标识唯一一条记录|-|
|name|string|否|记录文章的名称|-|
|category|string|否|用于记录文章所属的栏目|该数据默认为未分类|
|content_path|string|否|用于记录该文章所在的文件路径|-|
|created_at|date|否|用于记录该文章的创建的时间|为第一次创建条目的时间|
|updated_at|date|否|用于记录该文章的更新的时间|为每次更新的时间|

---

### 1.3.2. cmsModel_user_account

#### 1.3.2.1. 数据表描述

该表用于保存用户的账户信息。包括用户名，密码md5码，邮箱，手机号码，权限等级，账户等级，账户积分，创建时间，更新时间。

#### 1.3.2.2. 数据表结构说明

|表项|数据类型|是否是主键|描述|注释|
|:---:|:---:|:---:|:---:|:---:|
|id|int auto_increment|是|用于标识唯一一条记录|-|
|user_name|string|否|记录当前用户的用户名|-|
|user_md5|string|否|记录当前用户的md5校验码|该校验码的生成规则是md5(userEmail:password),最终的校验手段是md5(md5(userEmail:password):随机给出的uuid)|
|user_email|string|否|用于记录该用户的邮箱|邮箱是用来注册的和登录的|
|user_phone|string|否|用于记录用户的手机号码|绑定了手机号码才会有这条信息|
|user_privilege_level|int|否|用于记录用户的权限等级|权限等级决定了用户所能够做的操作|
|user_account_level|int|否|用于记录用户的账号等级|账号等级决定了用户的权限等级|
|user_account_point|int|否|用于记录用户的账号积分数|积分数决定了账号的等级|
|created_at|date|否|用于记录该文章的创建的时间|为第一次创建条目的时间|
|updated_at|date|否|用于记录该文章的更新的时间|为每次更新的时间|

---

### 1.3.3. cmsModel_admin_account

#### 1.3.3.1. 数据表描述

该表用于保存管理员的账户信息。包括用户名，密码md5码，邮箱，手机号码，权限等级，创建时间，更新时间。

#### 1.3.3.2. 数据表结构说明

|表项|数据类型|是否是主键|描述|注释|
|:---:|:---:|:---:|:---:|:---:|
|id|int auto_increment|是|用于标识唯一一条记录|-|
|admin_name|string|否|记录当前用户的用户名|-|
|admin_md5|string|否|记录当前用户的md5校验码|该校验码的生成规则是md5(userEmail:password),最终的校验手段是md5(md5(userEmail:password):随机给出的uuid)|
|admin_email|string|否|用于记录该用户的邮箱|邮箱是用来注册的和登录的|
|admin_phone|string|否|用于记录用户的手机号码|绑定了手机号码才会有这条信息|
|admin_privilege_level|int|否|用于记录用户的权限等级|权限等级决定了用户所能够做的操作|
|created_at|date|否|用于记录该文章的创建的时间|为第一次创建条目的时间|
|updated_at|date|否|用于记录该文章的更新的时间|为每次更新的时间|