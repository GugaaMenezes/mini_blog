CREATE TABLE "comments" (
  "id" integer NOT NULL,
  "article_id" integer NOT NULL,
  "id_user" integer NOT NULL,
  "content_comment" text NOT NULL,
  "created_at" datetime NOT NULL,
  "status_comment" bool NOT NULL,
  PRIMARY KEY ("id"),
  CONSTRAINT "fk_comments_miniblog_article_1" FOREIGN KEY ("article_id") REFERENCES "miniblog_article" ("id"),
  CONSTRAINT "fk_comments_users_1" FOREIGN KEY ("id_user") REFERENCES "users" ("id")
);

CREATE TABLE "miniblog_article" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "title" varchar(255) NOT NULL,
  "subtitle" varchar(255) NOT NULL,
  "type" integer NOT NULL,
  "content" text NOT NULL,
  "status" integer NOT NULL,
  "created_at" datetime NOT NULL,
  "id_user" integer NOT NULL,
  "status_article" bool NOT NULL,
  "created_users" integer NOT NULL,
  CONSTRAINT "fk_miniblog_article_users_1" FOREIGN KEY ("created_users") REFERENCES "users" ("id")
);
INSERT INTO "sqlite_sequence" (name, seq) VALUES ('miniblog_article', '17');

CREATE TABLE "miniblog_article_keyword_set" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "article_id" bigint NOT NULL,
  "keyword_id" bigint NOT NULL,
  FOREIGN KEY ("keyword_id") REFERENCES "miniblog_keyword" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "sqlite_sequence" (name, seq) VALUES ('miniblog_article_keyword_set', '26');
CREATE INDEX "miniblog_article_keyword_set_article_id_07126345"
ON "miniblog_article_keyword_set" (
  "article_id" ASC
);
CREATE UNIQUE INDEX "miniblog_article_keyword_set_article_id_keyword_id_b08a48b8_uniq"
ON "miniblog_article_keyword_set" (
  "article_id" ASC,
  "keyword_id" ASC
);
CREATE INDEX "miniblog_article_keyword_set_keyword_id_18509609"
ON "miniblog_article_keyword_set" (
  "keyword_id" ASC
);

CREATE TABLE "miniblog_keyword" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" varchar(255) NOT NULL
);
INSERT INTO "sqlite_sequence" (name, seq) VALUES ('miniblog_keyword', '19');

CREATE TABLE "users" (
  "id" integer NOT NULL,
  "username" text NOT NULL,
  "password" text NOT NULL,
  "email_username" text NOT NULL,
  "created_at" datetime NOT NULL,
  "status_user" bool NOT NULL,
  PRIMARY KEY ("id")
);

