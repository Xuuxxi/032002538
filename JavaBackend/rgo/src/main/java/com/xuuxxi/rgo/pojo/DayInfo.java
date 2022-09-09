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

    private String cur_time;

    private String new_add;

    private String new_null;

    private String pro_add;

    private String pro_null;

    private String hk_total;

    private String tw_total;

    private String am_total;
}
