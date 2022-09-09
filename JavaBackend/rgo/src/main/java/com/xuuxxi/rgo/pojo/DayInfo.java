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

    private Long id;

    private String curTime;

    private String newAdd;

    private String newNull;

    private String proAdd;

    private String proNull;

    private String hkTotal;

    private String twTotal;

    private String amTotal;
}
