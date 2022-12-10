CREATE TABLE userinfo (
    user_number SERIAL NOT NULL,
    user_id text UNIQUE NOT NULL,
    handleName text DEFAULT 'GUEST',
    password text NOT NULL,
    PRIMARY KEY (user_number)
);
CREATE TABLE ranking (
    response_id SERIAL NOT NULL,
    user_number int DEFAULT 99999999,
    isCorrect boolean NOT NULL,
    PRIMARY KEY (response_id),
    FOREIGN KEY (user_number) REFERENCES userinfo (user_number)
);
insert into userinfo(user_number, user_id, password)
values(1, 'admin', 'admin');
insert into ranking(user_number, isCorrect)
values(1, true);
insert into ranking(user_number, isCorrect)
values(1, false);
insert into ranking(user_number, isCorrect)
values(1, true);
insert into ranking(user_number, isCorrect)
values(1, false);