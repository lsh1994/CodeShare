/*
Navicat MySQL Data Transfer

Source Server         : mytest
Source Server Version : 50718
Source Host           : localhost:3306
Source Database       : noname

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2017-05-19 20:03:46
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for good
-- ----------------------------
DROP TABLE IF EXISTS `good`;
CREATE TABLE `good` (
  `gid` varchar(11) NOT NULL COMMENT '商品ID',
  `title` varchar(255) DEFAULT NULL COMMENT '商品标签',
  `price` double(255,0) DEFAULT NULL,
  `biaoqian` varchar(255) DEFAULT NULL COMMENT '商品整体标签',
  `haopingdu` varchar(255) DEFAULT NULL,
  `time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '添加记录时间',
  PRIMARY KEY (`gid`),
  UNIQUE KEY `gid` (`gid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for pinglun
-- ----------------------------
DROP TABLE IF EXISTS `pinglun`;
CREATE TABLE `pinglun` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(255) DEFAULT NULL COMMENT '用户名',
  `gid` varchar(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `xinde` text,
  `yanse` varchar(255) DEFAULT NULL,
  `chima` varchar(255) DEFAULT NULL,
  `biaoqian` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `gid` (`gid`),
  CONSTRAINT `pinglun_ibfk_1` FOREIGN KEY (`gid`) REFERENCES `good` (`gid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3521 DEFAULT CHARSET=utf8;
