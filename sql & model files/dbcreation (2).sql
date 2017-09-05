use colog;

DROP TABLE IF EXISTS `app_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dob` date NOT NULL,
  `mobile_no` varchar(20) NOT NULL,
  `education_place` varchar(40) NOT NULL,
  `education_field` varchar(40) NOT NULL,
  `employment_place` varchar(40) NOT NULL,
  `employment_designation` varchar(40) NOT NULL,
  `occupation` varchar(40) NOT NULL,
  `residence_place` varchar(60) NOT NULL,
  `country` varchar(30) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mobile_no` (`mobile_no`),
  UNIQUE KEY `user_id` (`user_id`)/*,
  CONSTRAINT `app_userprofile_user_id_4ed9bee8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)*/
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;



CREATE TABLE `post` (
  `pt_id` int(11) NOT NULL AUTO_INCREMENT,
  `text` TEXT NOT NULL,
  `likes` int(11) NOT NULL,
  `up_id` int(11) NOT NULL,
  'time' datetime NOT NULL,
  'title' varchar(140) NOT NULL,
  PRIMARY KEY (`pt_id`),
  CONSTRAINT `post_up_id_fk_app_userprofile_id` FOREIGN KEY (`up_id`) REFERENCES `app_userprofile` (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `comment` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `text` text NOT NULL,
  `likes` int(11) NOT NULL,
  `pt_id` int(11) NOT NULL,
  PRIMARY KEY (`c_id`),
  CONSTRAINT `comment_pt_id_fk_post_pt_id` FOREIGN KEY (`pt_id`) REFERENCES `post` (`pt_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

#change fkey above

CREATE TABLE `topic` (
  `name` varchar(120) NOT NULL,
  `t_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`t_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `follows` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `up_id_follower` int(11) NOT NULL,
  `up_id_following` int(11) NOT NULL,
  PRIMARY KEY (`f_id`),
  CONSTRAINT `follows_up_id_follower_fk_app_userprofile_id` FOREIGN KEY (`up_id_follower`) REFERENCES `app_userprofile` (`id`),
  CONSTRAINT `follows_up_id_following_fk_app_userprofile_id` FOREIGN KEY (`up_id_following`) REFERENCES `app_userprofile` (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `has_interest` (
  `h_i_id` int(11) NOT NULL AUTO_INCREMENT,
  `up_id` int(11) NOT NULL,
  `t_id` int(11) NOT NULL,
  PRIMARY KEY (`h_i_id`),
  CONSTRAINT `has_interest_up_id_fk_app_userprofile_id` FOREIGN KEY (`up_id`) REFERENCES `app_userprofile` (`id`),
  CONSTRAINT `has_interest_t_id_fk_topic_t_id` FOREIGN KEY (`t_id`) REFERENCES `topic` (`t_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `has_tags` (
  `h_t_id` int(11) NOT NULL AUTO_INCREMENT,
  `pt_id` int(11) NOT NULL,
  `t_id` int(11) NOT NULL,
  PRIMARY KEY (`h_t_id`),
  CONSTRAINT `has_tags_pt_id_fk_post_pt_id` FOREIGN KEY (`pt_id`) REFERENCES `post` (`pt_id`),
  CONSTRAINT `has_tags_t_id_fk_topic_t_id` FOREIGN KEY (`t_id`) REFERENCES `topic` (`t_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
