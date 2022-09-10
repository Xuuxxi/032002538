package com.xuuxxi.rgo.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;

/**
 * @Author: Xuuxxi
 * @Date: 2022/9/10
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
@TableName("cur_day")
public class CurDay implements Serializable {
    private static final long serialVersionUID = 1L;

    private Long id;

    private String curTime;
}
