/*
订单数据截止到12月，优惠券数据截止到1219
*/
select count(*) from coupon_info where bid in(2,3,4,7,8);
-- 7月优惠券数量
select couponid from coupon_info where bid in(2) and created >= "2018-07-01" and created <= "2018-08-01";



/*
机票sql脚本
*/
select count(*) from coupon_info where bid in(2) and created >= 2018-07-01;
select couponid from coupon_info where bid in(2) and created >= 2018-07-01;
-- 总使用数量
select couponNum as "礼券id", c.name as "礼券名称", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all o,coupon_info c where
    couponNum in (select couponid from coupon_info where bid in(2))
    and o."couponNum" == c.couponid
    and orderStatus in (20,22,30)
    group by couponNum;
    
-- 7月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all o,coupon_info c where
    couponNum in (select couponid from coupon_info where bid in(2))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-07-01" and orderTime < "2018-08-01"
    group by couponNum;
    
-- 8月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(2))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-08-01" and orderTime < "2018-09-01"
    group by couponNum;
    
-- 9月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(2))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-09-01" and orderTime < "2018-10-01"
    group by couponNum;
    
-- 10月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(2))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-10-01" and orderTime < "2018-11-01"
    group by couponNum;
  
-- 11月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(2))
    and orderStatus in (20,22,30)
    and orderTime >= '2018-11-01' and orderTime < '2018-12-01'
    group by couponNum;  

-- 总未使用礼券
select couponid from coupon_info where bid = 2
    and created >= '2018-07-01'
    and couponid not in(select couponNum from orderInfo_all);
    

    

/*
火车票sql脚本
*/
select counet(*) from coupon_info where bid in(3) and created >= "2018-07-01";
-- 总使用数量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(3) and created >= "2018-07-01")
    and orderStatus in (20,22,30)
    group by couponNum;
    
-- 7月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(3))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-07-01" and orderTime < "2018-08-01"
    group by couponNum; 

-- 8月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(3))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-08-01" and orderTime < "2018-09-01"
    group by couponNum;
    
-- 9月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(3))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-09-01" and orderTime < "2018-10-01"
    group by couponNum;
    
-- 10月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(3))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-10-01" and orderTime < "2018-11-01"
    group by couponNum;
  
-- 11月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(3))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-11-01" and orderTime < "2018-12-01"
    group by couponNum; 

/*
酒店sql脚本
*/
select count(*) from coupon_info where bid in(4) and created >= "2018-07-01";
-- 总使用数量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(4) and created >= "2018-07-01")
    and orderStatus in (20,22,30)
    group by couponNum;

-- 7月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(4))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-07-01" and orderTime < "2018-08-01"
    group by couponNum; 
    
-- 8月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(2))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-08-01" and orderTime < "2018-09-01"
    group by couponNum;
    
-- 9月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(2))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-09-01" and orderTime < "2018-10-01"
    group by couponNum;
    
-- 10月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(2))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-10-01" and orderTime < "2018-11-01"
    group by couponNum;
  
-- 11月使用量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(2))
    and orderStatus in (20,22,30)
    and orderTime >= "2018-11-01" and orderTime < "2018-12-01"
    group by couponNum;  




/*
专车sql脚本
*/
select count(*) from coupon_info where bid in(7) and created >= 2018-07-01;
-- 总使用数量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(7) and created >= "2018-07-01")
    and orderStatus in (20,22,30)
    group by couponNum;
    

/*
门票sql脚本
*/
select count(*) from coupon_info where bid in(8) and created >= "2018-07-01";
-- 总使用数量
select couponNum as "礼券id", count(orderNum) as "使用总数量", SUM(couponAmount) as "使用总金额" from orderInfo_all where 
    couponNum in (select couponid from coupon_info where bid in(8) and created >= "2018-07-01")
    and orderStatus in (20,22,30)
    group by couponNum;



--
select * from orderInfo where couponid in (select couponid from coupon_info where bid=3);

select count(*) from orderInfo_all where couponNum=496 and orderStatus in (20,22,30)