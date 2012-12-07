

-- ed2k 数据库设计

CREATE table if not exists `ed2k`(
	`id` int(10) not null auto_increment,
	`verycdid` int(10) not null,
	`title` varchar(1000) not null,
	``
)

-- count table
CREATE table if not exists 'count'(
	'id' int not null auto_increment,
	'category'
	'count' int(10) not null,
)