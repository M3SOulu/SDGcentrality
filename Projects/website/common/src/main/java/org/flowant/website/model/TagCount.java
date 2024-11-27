package org.flowant.website.model;

import org.springframework.data.cassandra.core.mapping.Element;
import org.springframework.data.cassandra.core.mapping.Tuple;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.experimental.Accessors;

@Data
@Accessors(chain=true)
@AllArgsConstructor(staticName="of")
@NoArgsConstructor
@Tuple
public class TagCount {

    @Element(0)
    String tag;

    @Element(1)
    long searched;

    @Element(2)
    long referred;

}
