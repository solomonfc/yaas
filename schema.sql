drop table if exists gl_book cascade;
create table gl_book(
	book_id					varchar(10),
	book_name				varchar(40)
);


drop table if exists gl_acct cascade;
create table gl_acct(
	acct_code				varchar(10),
	acct_name				varchar(50),
	acct_lvl				varchar(10),
	parent_acct_code		varchar(10),
	is_leaf					varchar(10)
);


drop table if exists gl_vouch cascade;
create table gl_vouch(
	vouch_id				varchar(32),
	vouch_no				varchar(32)
);


drop table if exists gl_entry cascade;
create table gl_entry(
	vouch_id				varchar(32),
	entry_seq				varchar(10),
	acct_code				varchar(10),
	dr_amt					varchar(40),
	cr_amt					varchar(40)
);


drop table if exists gl_acct_sum cascade;
create table gl_acct_sum(
	period_no				varchar(10),
	acct_code				varchar(40),
	dr_opening				varchar(40),
	cr_opening				varchar(40),
	dr_amt					varchar(40),
	cr_amt					varchar(40),
	dr_closing				varchar(40),
	cr_closing				varchar(40)
);