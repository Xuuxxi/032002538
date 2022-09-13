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
 * 日期对应url控制
 */
@RestController
@RequestMapping("/urlInfo")
public class UrlInfoController {
    @Resource
    private UrlInfoMapper mapper;

    // 查
    @PostMapping("/getInfo")
    public UrlInfo getInfo(@RequestBody UrlInfo urlInfo){
        UrlInfo res = null;
        System.out.println(urlInfo);
        if(urlInfo.getCurTime() != null) {
            LambdaQueryWrapper<UrlInfo> wrapper = new LambdaQueryWrapper<>();
            wrapper.eq(UrlInfo::getCurTime,urlInfo.getCurTime());
            res = mapper.selectOne(wrapper);
        }else{
            LambdaQueryWrapper<UrlInfo> wrapper = new LambdaQueryWrapper<>();
            wrapper.eq(UrlInfo::getUrl,urlInfo.getUrl());
            res = mapper.selectOne(wrapper);
        }
        return res;
    }

    // 增
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
