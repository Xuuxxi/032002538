package com.xuuxxi.rgo.controlelr;

/**
 * @Author: Xuuxxi
 * @Date: 2022/9/9
 */

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.xuuxxi.rgo.common.R;
import com.xuuxxi.rgo.mapper.DayInfoMapper;
import com.xuuxxi.rgo.pojo.CurDay;
import com.xuuxxi.rgo.pojo.DayInfo;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.List;

// 查询对应日期的爬虫信息
@RestController
@RequestMapping("/dayInfo")
@Slf4j
public class DayInfoController {
    @Resource
    private DayInfoMapper mapper;

    // 查
    @PostMapping("/getInfo")
    public DayInfo getInfo(@RequestBody DayInfo dayInfo){
        log.info("curTime is " + dayInfo.getCurTime());
        LambdaQueryWrapper<DayInfo> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(DayInfo::getCurTime,dayInfo.getCurTime());
        return mapper.selectOne(wrapper);
    }

    // 增
    @PostMapping("/setInfo")
    public String setInfo(@RequestBody DayInfo dayInfo){
        LambdaQueryWrapper<DayInfo> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(DayInfo::getCurTime,dayInfo.getCurTime());
        List<DayInfo> t = mapper.selectList(wrapper);
        if (t.size() == 0) {
            mapper.insert(dayInfo);
        }else return "false";
        return "Success";
    }
}
