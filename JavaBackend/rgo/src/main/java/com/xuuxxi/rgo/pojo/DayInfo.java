package com.xuuxxi.rgo.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;
import java.time.LocalDateTime;

/**
 * @Author: Xuuxxi
 * @Date: 2022/9/9
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
@TableName("day_info")
public class DayInfo implements Serializable {
    private static final long serialVersionUID = 1L;

    // 雪花算法自动生成
    private Long id;

    // 当前日期
    private String curTime;

    // 全国新增确诊
    private String newAdd;

    // 全国新增无症状
    private String newNull;

    // 各省份新增确诊状况
    private String proAdd;

    // 各省份新增无症状状况
    private String proNull;

    // 香港总确诊
    private String hkTotal;

    // 台湾总确诊
    private String twTotal;

    // 澳门总确诊
    private String amTotal;
}
