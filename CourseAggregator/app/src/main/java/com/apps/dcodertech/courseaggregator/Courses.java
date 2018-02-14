package com.apps.dcodertech.courseaggregator;

import java.io.Serializable;

/**
 * Created by dhruv on 1/31/2018.
 */

public class Courses implements Serializable {
    private String title,certificates,duration,hours;
    private String institution,language,link,teacher,provider;
    public Courses(String title,String certificates,String duration,String hours,String institution,String language,String link,String teacher,String provider){
        this.title=title;
        this.certificates=certificates;
        this.duration=duration;
        this.hours=hours;
        this.institution=institution;
        this.language=language;
        this.link=link;
        this.teacher=teacher;
        this.provider=provider;
    }

    public String getTitle() {
        return title;
    }

    public String getCertificates() {
        return certificates;
    }

    public String getDuration() {
        return duration;
    }

    public String getHours() {
        return hours;
    }

    public String getInstitution() {
        return institution;
    }

    public String getLanguage() {
        return language;
    }

    public String getLink() {
        return link;
    }

    public String getProvider() {
        return provider;
    }

    public String getTeacher() {
        return teacher;
    }
}

