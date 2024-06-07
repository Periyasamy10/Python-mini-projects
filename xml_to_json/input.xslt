<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="/">
    <output>
      <xsl:apply-templates select="catalog"/>
    </output>
  </xsl:template>

  <xsl:template match="catalog">
    <catalog>
      <xsl:attribute name="id"><xsl:value-of select="@id"/></xsl:attribute>
      <xsl:apply-templates select="book"/>
    </catalog>
  </xsl:template>

  <xsl:template match="book">
    <book>
      <xsl:attribute name="id"><xsl:value-of select="@id"/></xsl:attribute>
      <title><xsl:value-of select="title"/></title>
      <author><xsl:value-of select="author"/></author>
      <price><xsl:value-of select="price"/></price>
      <category><xsl:value-of select="category"/></category>
    </book>
  </xsl:template>

</xsl:stylesheet>
