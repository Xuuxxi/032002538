package com.xuuxxi.rgo.controlelr;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.xuuxxi.rgo.mapper.CurDayMapper;
import com.xuuxxi.rgo.pojo.CurDay;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;

/**
 * @Author: Xuuxxi
 * @Date: 2022/9/10
 */
@RestController
@RequestMapping("/curDay")
public class CurDayController {
    @Resource
    private CurDayMapper mapper;

    @GetMapping("/getCurDay")
    public String getCurDay(){
        return mapper.selectById(1L).getCurTime();
    }

    @PostMapping("/setCurDay")
    public String setCurDay(@RequestBody CurDay curDay){
        curDay.setId(1L);
        mapper.insert(curDay);
        return "Success";
    }

    @PutMapping("/updCurDay")
    public String updCurDay(@RequestBody CurDay curDay){
        curDay.setId(1L);
        mapper.updateById(curDay);
        return "Success";
    }
}
