/**************************************************************************
--dbname: tongpao_db
--create db: create database tongpao_db default charset=utf8;
--import sql: mysql -hhostname -uuseranme -p tongpao_db < tongpao_db.sql
**************************************************************************/
drop table if exists b_user;
create table b_user(
    u_id int unsigned primary key auto_increment,
    username char(64),
    passwd char(64),
    email char(64),
    birthday int,
    pic_id int comment '头像图片id',
    description text comment '简单摘要',
    research_fields varchar(255) comment '研究领域,每条以逗号分割',
    created int unsigned not null default 0,
    updated int unsigned not null default 0,
    key username(username)
)engine = innodb default charset=utf8;

drop table if exists b_perm_level;
create table b_perm_level(
    id int unsigned primary key auto_increment,
    level tinyint unsigned comment '权限级别',
    description char(64) comment '权限描述',
    created int unsigned not null default 0,
    updated int unsigned not null default 0
)engine = innodb default charset=utf8;

drop table if exists b_permissons;
create table b_permissons(
    id int unsigned primary key auto_increment,
    level_id tinyint unsigned comment '权限级别',
    u_id int unsigned not null default 0,
    created int unsigned not null default 0,
    updated int unsigned not null default 0,
    key u_id_level_id (u_id, level_id)
)engine = innodb default charset=utf8;

drop table if exists b_team_works;
create table b_team_works(
    id int unsigned primary key auto_increment,
    work_name varchar(100) comment '作品名',
    work_intro text comment '作品介绍',
    team_leader char(64) comment '组长名',
    team_members varchar(64) comment '合作成员, 用户名以逗号分开',
    start_time int unsigned not null default 0 comment '开发开始时间',
    end_time int unsigned not null default 0 comment '开发结束时间',
    honor text comment '获得荣誉',
    pic_ids varchar(254) comment '图片id, 逗号分开',
    relate_links text comment '相关连接,没条以"标题:链接","标题:连接"格式',
    created int unsigned not null default 0,
    updated int unsigned not null default 0,
    key work_name(work_name)
)engine = innodb default charset=utf8;

drop table if exists b_news;
create table b_news(
    id int unsigned primary key auto_increment,
    user_id int unsigned not null default 0,
    username char(64),
    title varchar(254),
    content text,
    pic_ids varchar(254) comment '新闻图片id，逗号分隔',
    is_display enum('hidden','show') not null default 'hidden',
    created int unsigned not null default 0,
    updated int unsigned not null default 0,
    key title(title)
)engine = innodb default charset=utf8;

drop table if exists b_message;
create table b_message(
    id int unsigned primary key auto_increment,
    email char(64),
    content text,
    created int unsigned not null default 0,
    updated int unsigned not null default 0
)engine = innodb default charset=utf8;

drop table if exists b_pictures;
create table b_pictures(
    id int unsigned primary key auto_increment,
    pic_show_name char(40) unique key comment '图片显示名字,用sha1算法计算原图片名字',
    created int unsigned not null default 0,
    updated int unsigned not null default 0
)engine = innodb default charset=utf8;
