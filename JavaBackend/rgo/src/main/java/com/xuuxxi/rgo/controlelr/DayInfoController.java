package com.xuuxxi.rgo.controlelr;

/**
 * @Author: Xuuxxi
 * @Date: 2022/9/9
 */

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.xuuxxi.rgo.common.R;
import com.xuuxxi.rgo.mapper.DayInfoMapper;
import com.xuuxxi.rgo.pojo.DayInfo;
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

    @GetMapping("/getInfo/{curDay}")
    public R<DayInfo> getInfo(@PathVariable String curDay){
        QueryWrapper<DayInfo> wrapper = new QueryWrapper<>();
        wrapper.eq("cur_time",curDay);
        DayInfo dayInfo = mapper.selectOne(wrapper);
        return R.success(dayInfo);
    }

    @PostMapping("/setInfo")
    public String setInfo(@RequestBody DayInfo dayInfo){
        QueryWrapper<DayInfo> wrapper = new QueryWrapper<>();
        wrapper.eq("cur_time",dayInfo.getCur_time());
        List<DayInfo> t = mapper.selectList(wrapper);
        if (t.size() == 0) {
            mapper.insert(dayInfo);
        }else return "false";
        return "Success";
    }
}
