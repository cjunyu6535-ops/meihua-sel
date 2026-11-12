#!/usr/bin/env python3
"""
梅花易數確定性排卦驗算引擎 (Mei Hua Yi Shu Calculation Engine)
純標準庫、零外部依賴
Usage: python3 meihua_calc.py <N1> <N2> [N3]
"""

import sys

TRIGRAMS = {
    1: ("乾", "金", "天"),
    2: ("兌", "金", "澤"),
    3: ("離", "火", "日"),
    4: ("震", "木", "雷"),
    5: ("巽", "木", "風"),
    6: ("坎", "水", "雨"),
    7: ("艮", "土", "山"),
    8: ("坤", "土", "地"),
}

ELEMENT_RELS = {
    ("金", "金"): "比和", ("木", "木"): "比和", ("水", "水"): "比和", ("火", "火"): "比和", ("土", "土"): "比和",
    ("金", "木"): "體剋用", ("木", "土"): "體剋用", ("土", "水"): "體剋用", ("水", "火"): "體剋用", ("火", "金"): "體剋用",
    ("木", "金"): "用剋體", ("土", "木"): "用剋體", ("水", "土"): "用剋體", ("火", "水"): "用剋體", ("金", "火"): "用剋體",
    ("金", "水"): "體生用", ("水", "木"): "體生用", ("木", "火"): "體生用", ("火", "土"): "體生用", ("土", "金"): "體生用",
    ("水", "金"): "用生體", ("木", "水"): "用生體", ("火", "木"): "用生體", ("土", "火"): "用生體", ("金", "土"): "用生體",
}

def calc_meihua(n1, n2, n3=None):
    upper_num = n1 % 8 if n1 % 8 != 0 else 8
    lower_num = n2 % 8 if n2 % 8 != 0 else 8
    
    total_sum = n1 + n2 + (n3 if n3 is not None else 0)
    moving_line = total_sum % 6 if total_sum % 6 != 0 else 6

    upper_tri = TRIGRAMS[upper_num]
    lower_tri = TRIGRAMS[lower_num]

    if moving_line in [1, 2, 3]:
        ti_tri = upper_tri
        yong_tri = lower_tri
        ti_pos = "上卦"
    else:
        ti_tri = lower_tri
        yong_tri = upper_tri
        ti_pos = "下卦"

    rel = ELEMENT_RELS.get((ti_tri[1], yong_tri[1]), "未知")

    print(f"--- 梅花易數排卦驗算結果 ---")
    print(f"上卦: {upper_tri[0]} ({upper_tri[1]})")
    print(f"下卦: {lower_tri[0]} ({lower_tri[1]})")
    print(f"動爻: 第 {moving_line} 爻")
    print(f"體卦: {ti_tri[0]} ({ti_tri[1]}, 位在{ti_pos})")
    print(f"用卦: {yong_tri[0]} ({yong_tri[1]})")
    print(f"五行生剋 (體/用): {rel}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 meihua_calc.py <N1> <N2> [N3]")
        sys.exit(1)
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    n3 = int(sys.argv[3]) if len(sys.argv) > 3 else None
    calc_meihua(n1, n2, n3)
