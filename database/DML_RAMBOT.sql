INSERT INTO TB_BOT (BOT_ID, DESCRIPTION) VALUES 
(NULL, 'INSTAGRAM'), 
(NULL, 'FACEBOOK');

INSERT INTO TB_URL (URL_ID, URL) VALUES 
(NULL, 'https://www.instagram.com/accounts/login/'),
(NULL, 'https://www.facebook.com/'),
(NULL, 'https://www.instagram.com/');

INSERT INTO TB_ACTION (ACTION_ID, DESCRIPTION) VALUES 
(NULL, 'LOGIN'),
(NULL, 'FOLLOW'),
(NULL, 'FOLLOWING'),
(NULL, 'FOLLOWERS'),
(NULL, 'LIKE'),
(NULL, 'STORY'),
(NULL, 'DOWNLOAD');

INSERT INTO TB_ACTION_URL (ACTION_URL_ID, ACTION_ID, URL_ID) VALUES
(NULL, 1,1),
(NULL, 1,2),
(NULL, 2,3),
(NULL, 3,3),
(NULL, 4,3),
(NULL, 5,3),
(NULL, 6,3),
(NULL, 7,3);

INSERT INTO TB_XPATH (XPATH_ID, XPATH) VALUES 
(NULL, '//form[1]/div[1]/div/div/input'), 
(NULL, '//form[1]/div[2]/div/div/input'),
(NULL, '//form[1]/table/tbody/tr[2]/td[1]/input'),
(NULL, '//*[@id="pass"]'),
(NULL, '//button[contains(text(),"Follow")]'),
(NULL, '/html[1]/body[1]/span[1]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[3]/a[1]'),
(NULL, '/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]'),
(NULL, '/html[1]/body[1]/span[1]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[3]/a[1]/span[1]'),
(NULL, '/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]'),
(NULL, '/html[1]/body[1]/span[1]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[2]/a[1]'),
(NULL, '/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]'),
(NULL, '/html[1]/body[1]/span[1]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[2]/a[1]/span[1]'),
(NULL, '/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]'),
(NULL, '/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/ul[1]/div[1]'),
(NULL, '/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/ul[1]/div[1]'),
(NULL, '/html[1]/body[1]/span[1]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[1]/span[1]/span[1]'),
(NULL, '/html[1]/body[1]/span[1]/section[1]/main[1]/div[1]/div[3]/article[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[2]'),
(NULL, '/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/article[1]/div[2]/section[1]/span[1]/button[1]/span[1]'),
(NULL, '//a[contains(@class,"HBoOv coreSpriteRightPaginationArrow")]'),
(NULL, '/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/article[1]/div[2]/section[3]/div[1]/form[1]/textarea[1]'),
(NULL, '/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/img[1]');


INSERT INTO TB_BOT_ACTION_URL (BOT_ACTION_URL_ID, BOT_ID, ACTION_URL_ID) VALUES 
(NULL, 1, 1),
(NULL, 2, 2),
(NULL, 1, 3),
(NULL, 1, 4),
(NULL, 1, 5),
(NULL, 1, 6),
(NULL, 1, 7),
(NULL, 1, 8);

INSERT INTO TB_BOT_ACTION_URL_XPATH (BOT_ACTION_URL_ID, XPATH_ID, POSITION, DESCRIPTION) VALUES 
(1,1,1, 'INSTAGRAM-LOGIN-USERNAME'), 
(1,2,2, 'INSTAGRAM-LOGIN-PASSWORD'),
(2,3,1, 'FACEBOOK-LOGIN-USERNAME'),
(2,4,2, 'FACEBOOK-LOGIN-PASSWORD'),
(3,5,1, 'INSTAGRAM-FOLLOW-FOLLOW_USER_BUTTON'),
(4,6,1, 'INSTAGRAM-FOLLOWING-USER_FOLLOWING_BUTTON'),
(4,7,2, 'INSTAGRAM-FOLLOWING-USER_FOLLOWING_MODAL'),
(4,8,3, 'INSTAGRAM-FOLLOWING-USER-TOTAL_FOLLOWING'),
(4,9,4, 'INSTAGRAM-FOLLOWING_USER_SCROLL_FOLLOWING'),
(5,10,1, 'INSTAGRAM-FOLLOWERS_USER_FOLLOWERS_BUTTON'),
(5,11,2, 'INSTAGRAM-FOLLOWERS-USER_FOLLOWERS_MODAL'),
(5,12,3, 'INSTAGRAM_FOLLOWERS_USER_TOTAL_FOLLOWERS'),
(5,13,4, 'INSTAGRAM-FOLLOWERS-USER-SCROLL_FOLLOWERS'),
(4,14,5, 'INSTAGRAM-FOLLOWING_USER_DINAMIC_DIV'),
(5,15,5, 'INSTAGRAM-FOLLOWERS_USER_DINAMIC_DIV'),
(6,16,1, 'INSTAGRAM-LIKE-POSTS-TOTAL_POSTS'),
(6,17,2, 'INSTAGRAM-LIKE-POSTS_FIRST_POST'),
(6,18,3, 'INSTAGRAM_LIKE_POSTS_LIKE-POST'),
(6,19,4, 'INSTAGRAM_LIKE_POST_NEXT_POST'),
(6,20,5, 'INSTAGRAM-LIKE_POST_COMMENT'),
(8,16,1, 'INSTAGRAM-DOWNLOAD-POSTS-TOTAL-POSTS'),
(8,17,2, 'INSTAGRAM-DOWNLOAD-POSTS-FIRST-POST'),
(8,21,3, 'INSTAGRAM-DOWNLOAD-POSTS-POST_SOURCE-POST'),
(8,19,4, 'INSTAGRAM-DOWNLOAD-POSTS-NEXT-POST');

