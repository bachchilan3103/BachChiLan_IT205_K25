import logging

logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

def get_discount_rate(tier: str, quantity: int) -> float:
    logger.debug(f"Tính chiết khấu cho hạng {tier} với số lượng {quantity}")

    if quantity <= 0:
        logger.error("Số lượng sản phẩm không hợp lệ (<= 0)")
        raise ValueError("Quantity must be positive")
    if tier == "silver":
        rate = 0.05
    elif tier == "gold":
        rate = 0.10
    elif tier == "diamond":
        rate = 0.15
    else:
        rate = 0.0
    if quantity >= 50:
        rate += 0.05 
        logger.info("Áp dụng thưởng thêm 5% cho số lượng >= 50")
        
    logger.debug(f"Tỷ lệ chiết khấu cuối cùng: {rate}")
    return rate


def calculate_agency_total(price: float, quantity: int, tier: str) -> float:
    if price < 0:
        raise ValueError("Đơn giá không được âm")

    rate = get_discount_rate(tier, quantity)
    final_price = price * (1 - rate) * quantity

    logger.info(
        f"Kết quả: Tổng tiền = {final_price:.2f} VND "
        f"(Chiết khấu {rate*100:.1f}%)"
    )
    return final_price




try:
    calculate_agency_total(100, 50, "silver")     
    calculate_agency_total(100, -5, "diamond")   
except ValueError as error:
    logger.error(f"Lỗi dữ liệu đầu vào: {error}")



