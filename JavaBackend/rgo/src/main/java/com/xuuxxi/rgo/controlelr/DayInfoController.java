package com.xuuxxi.rgo.controlelr;

/**
 * @Author: Xuuxxi
 * @Date: 2022/9/9
 */

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.xuuxxi.rgo.common.R;
import com.xuuxxi.rgo.mapper.DayInfoMapper;
import com.xuuxxi.rgo.pojo.DayInfo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.List;

/**
 * let config = {
 *         headers: {'Content-Type': "multipart/json, charset=UTF-8"}
 *     };
 *     let data = {
 *         fileName: '我爱你中国'
 *     };
 *     this.$axios
 *     .post('/api/file/testconttype', data, config);
 */

@RestController
@RequestMapping("/dayInfo")
public class DayInfoController {
    @Resource
    private DayInfoMapper mapper;

    @GetMapping("/getInfo")
    public DayInfo getInfo(@RequestParam String curDay){
        LambdaQueryWrapper<DayInfo> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(DayInfo::getCurTime,curDay);
        return mapper.selectOne(wrapper);
    }

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
