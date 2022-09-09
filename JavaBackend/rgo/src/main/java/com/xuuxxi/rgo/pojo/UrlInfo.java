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
@TableName("url_info")
public class UrlInfo implements Serializable {
    private static final long serialVersionUID = 1L;

    private Long id;

    private String cur_time;

    private String url;
}
