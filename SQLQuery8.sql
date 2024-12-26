use [hotelreservationsystem]

create table services (
    service_id int identity(1,1) primary key,
    service_name varchar(50) not null,
    price money not null
);

create table rooms (
    room_num int identity(1,1) primary key,
    room_type varchar(50) not null,
    status varchar(20) not null check (status in ('available', 'occupied', 'maintenance')),
    price money not null
);

create table guest (
    guest_id int identity(1,1) primary key,
    phone varchar(15) check (phone like '[0-9]%'),
    f_name varchar(50) not null,
    l_name varchar(50) not null,
    email varchar(50) not null unique,
    address varchar(100),
    constraint chk_email_domain check (email like '%@gmail.com')
);

create table billing (
    bill_id int identity(1,1) primary key,
    cost money check (cost >= 0),
    payment_status varchar(20) not null default 'pending' check (payment_status in ('pending', 'paid', 'cancelled')),
    payment_date date not null default getdate()
);

create table booking (
    booking_id int identity(1,1) primary key,
    checkin_date date not null default getdate(),
    checkout_date datetime,
    bill_id int not null,
    room_num int not null,
    guest_id int not null,
    unique (bill_id),
    foreign key (bill_id) references billing(bill_id) on delete cascade,
    foreign key (room_num) references rooms(room_num) on delete set null,
    foreign key (guest_id) references guest(guest_id) on delete cascade
);

create table chossed_services (
    service_id int not null,
    booking_id int not null,
    service_date date not null default getdate(),
    primary key (service_id, booking_id),
    foreign key (service_id) references services(service_id) on delete cascade,
    foreign key (booking_id) references booking(booking_id) on delete cascade
);
