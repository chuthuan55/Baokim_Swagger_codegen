<?php
/**
 * InlineResponse2001
 *
 * PHP version 5
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * Installment docs API
 *
 * <a href='/baokim-firm-open-api-9050'>1: Function Check Installment Support </a>  <a href='/baokim-firm-open-api-9051'>2: Function Get Bank Loan Package </a>  <a href='/baokim-firm-open-api-9052'>3: Function Create Transaction </a>  <a href='/baokim-firm-open-api-9062'>4: Function Cancel order</a>  Private key and public key Baokim is currently using digital signature by RSA-SHA1  There are several ways to generate RSA key pairs.  Way 1:  Generate your RSA key pairs online: <a href=\"http://travistidwell.com/blog/2013/09/06/an-online-rsa-public-and-private-key-generator/\" target=\"_blank\">Generate now</a>  Way 2:  Using OpenSSL software for Windows:  Step 1: Download the software at:  http://slproweb.com/products/Win32OpenSSL.html. Partner should download the installer \"OpenSSL_Light-1_0_2k\". Then install in any directory, for example \"C:\\OpenSSLWin64\"  Step 2: Access \"C:\\OpenSSLWin64\\bin\" then open the command prompt. Type the command to declare the environment config.  set OPENSSL_CONF=C:\\OpenSSL-Win64\\bin\\openssl.cfg  Step 3: Generate private key and public key  openssl genrsa -aes256 -out c:\\opensslkeys\\partner\\partner_privatekey.pem 2048  openssl rsa –in c:\\opensslkeys\\partner\\partner_privatekey.pem -pubout >c:\\opensslkeys\\partner\\partner_publickey.pem  After successful pairing, Partner will send back to Baokim the public key to authenticate the signature that the Partner sends via the API
 *
 * OpenAPI spec version: 1.0.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 * Swagger Codegen version: 3.0.35-SNAPSHOT
 */
/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace Swagger\Client\Model;

use \ArrayAccess;
use \Swagger\Client\ObjectSerializer;

/**
 * InlineResponse2001 Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class InlineResponse2001 implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'inline_response_200_1';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'response_code' => 'int',
'response_message' => 'string',
'data' => '\Swagger\Client\Model\InlineResponse2001Data',
'signature' => 'string'    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'response_code' => null,
'response_message' => null,
'data' => null,
'signature' => null    ];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerTypes()
    {
        return self::$swaggerTypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerFormats()
    {
        return self::$swaggerFormats;
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'response_code' => 'ResponseCode',
'response_message' => 'ResponseMessage',
'data' => 'Data',
'signature' => 'Signature'    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'response_code' => 'setResponseCode',
'response_message' => 'setResponseMessage',
'data' => 'setData',
'signature' => 'setSignature'    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'response_code' => 'getResponseCode',
'response_message' => 'getResponseMessage',
'data' => 'getData',
'signature' => 'getSignature'    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$swaggerModelName;
    }

    

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['response_code'] = isset($data['response_code']) ? $data['response_code'] : null;
        $this->container['response_message'] = isset($data['response_message']) ? $data['response_message'] : null;
        $this->container['data'] = isset($data['data']) ? $data['data'] : null;
        $this->container['signature'] = isset($data['signature']) ? $data['signature'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets response_code
     *
     * @return int
     */
    public function getResponseCode()
    {
        return $this->container['response_code'];
    }

    /**
     * Sets response_code
     *
     * @param int $response_code response_code
     *
     * @return $this
     */
    public function setResponseCode($response_code)
    {
        $this->container['response_code'] = $response_code;

        return $this;
    }

    /**
     * Gets response_message
     *
     * @return string
     */
    public function getResponseMessage()
    {
        return $this->container['response_message'];
    }

    /**
     * Sets response_message
     *
     * @param string $response_message response_message
     *
     * @return $this
     */
    public function setResponseMessage($response_message)
    {
        $this->container['response_message'] = $response_message;

        return $this;
    }

    /**
     * Gets data
     *
     * @return \Swagger\Client\Model\InlineResponse2001Data
     */
    public function getData()
    {
        return $this->container['data'];
    }

    /**
     * Sets data
     *
     * @param \Swagger\Client\Model\InlineResponse2001Data $data data
     *
     * @return $this
     */
    public function setData($data)
    {
        $this->container['data'] = $data;

        return $this;
    }

    /**
     * Gets signature
     *
     * @return string
     */
    public function getSignature()
    {
        return $this->container['signature'];
    }

    /**
     * Sets signature
     *
     * @param string $signature signature
     *
     * @return $this
     */
    public function setSignature($signature)
    {
        $this->container['signature'] = $signature;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     *
     * @param integer $offset Offset
     * @param mixed   $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        if (defined('JSON_PRETTY_PRINT')) { // use JSON pretty print
            return json_encode(
                ObjectSerializer::sanitizeForSerialization($this),
                JSON_PRETTY_PRINT
            );
        }

        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}
