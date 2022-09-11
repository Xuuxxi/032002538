package com.xuuxxi.rgo.controlelr;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.xuuxxi.rgo.mapper.CurDayMapper;
import com.xuuxxi.rgo.pojo.CurDay;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;

/**
 * @Author: Xuuxxi
 * @Date: 2022/9/10
 * 查询目前用户访问的页面信息
 */

@RestController
@RequestMapping("/curDay")
public class CurDayController {
    @Resource
    private CurDayMapper mapper;

    // 查
    @GetMapping("/getCurDay")
    public String getCurDay(){
        return mapper.selectById(1L).getCurTime();
    }

    // 增
    @PostMapping("/setCurDay")
    public String setCurDay(@RequestBody CurDay curDay){
        curDay.setId(1L);
        mapper.insert(curDay);
        return "Success";
    }

    // 改
    @PutMapping("/updCurDay")
    public String updCurDay(@RequestBody CurDay curDay){
        curDay.setId(1L);
        mapper.updateById(curDay);
        return "Success";
    }
}
