package com.xuuxxi.rgo.controlelr;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.xuuxxi.rgo.mapper.UrlInfoMapper;
import com.xuuxxi.rgo.pojo.UrlInfo;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.List;

/**
 * @Author: Xuuxxi
 * @Date: 2022/9/9
 */
@RestController
@RequestMapping("/urlInfo")
public class UrlInfoController {
    @Resource
    private UrlInfoMapper mapper;

    @GetMapping("/getInfo")
    public String getInfo(@RequestParam String curDay){
        LambdaQueryWrapper<UrlInfo> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(UrlInfo::getCurTime,curDay);
        UrlInfo urlInfo = mapper.selectOne(wrapper);
        return urlInfo.getUrl();
    }

    @PostMapping("/setInfo")
    public String setInfo(@RequestBody UrlInfo urlInfo){
        LambdaQueryWrapper<UrlInfo> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(UrlInfo::getCurTime, urlInfo.getCurTime());
        List<UrlInfo> t = mapper.selectList(wrapper);
        if (t.size() == 0) {
            mapper.insert(urlInfo);
        }else return "False";
        return "Success";
    }
}
