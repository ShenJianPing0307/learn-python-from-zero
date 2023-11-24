create table author(
    id int primary key auto_increment comment '主键ID',
    username varchar(32) default null comment '作者姓名',
    email varchar(255) default null comment '邮箱'
    )charset=utf8 collate=utf8_general_ci engine=innodb comment '作者表';