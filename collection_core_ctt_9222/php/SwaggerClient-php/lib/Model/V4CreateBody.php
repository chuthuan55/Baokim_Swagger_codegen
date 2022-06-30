<?php
/**
 * V4CreateBody
 *
 * PHP version 5
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * Collection payments
 *
 * <img src=\"https://devtest.baokim.vn/collection/core_ctt/image/Picture1.png\" class=\"image-collection-payment\" /> <p><strong>Note:</strong></p> <p>+ In case PARTNER want to use collect via Virtual Account, PARTNER will need to buid:</p> <p style=\"padding-left: 50px;\">     - <a href=\"#operations-Virtual_Account_4\\.0-8442c69ffbaf4b3677a52fa3ebcef6d4\">Register virtual account</a> <br>     - <a href=\"#operations-Virtual_Account_4\\.0-1796c61005edee3976097a607fe9dbaa\">Update virtual account informations</a> <br>     - <a href=\"#operations-tag-Notice_of_collection_transaction\">Notice of collection transaction</a> <br> </p>
 *
 * OpenAPI spec version: 2.3 and 4.0
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
 * V4CreateBody Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class V4CreateBody implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'V4_create_body';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'request_id' => 'string',
'request_time' => 'string',
'partner_code' => 'string',
'acc_name' => 'string',
'collect_amount' => 'float',
'order_id' => 'string',
'expire_date' => 'string',
'bank' => 'string'    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'request_id' => null,
'request_time' => null,
'partner_code' => null,
'acc_name' => null,
'collect_amount' => null,
'order_id' => null,
'expire_date' => null,
'bank' => null    ];

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
        'request_id' => 'RequestId',
'request_time' => 'RequestTime',
'partner_code' => 'PartnerCode',
'acc_name' => 'AccName',
'collect_amount' => 'CollectAmount',
'order_id' => 'OrderId',
'expire_date' => 'ExpireDate',
'bank' => 'Bank'    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'request_id' => 'setRequestId',
'request_time' => 'setRequestTime',
'partner_code' => 'setPartnerCode',
'acc_name' => 'setAccName',
'collect_amount' => 'setCollectAmount',
'order_id' => 'setOrderId',
'expire_date' => 'setExpireDate',
'bank' => 'setBank'    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'request_id' => 'getRequestId',
'request_time' => 'getRequestTime',
'partner_code' => 'getPartnerCode',
'acc_name' => 'getAccName',
'collect_amount' => 'getCollectAmount',
'order_id' => 'getOrderId',
'expire_date' => 'getExpireDate',
'bank' => 'getBank'    ];

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
        $this->container['request_id'] = isset($data['request_id']) ? $data['request_id'] : null;
        $this->container['request_time'] = isset($data['request_time']) ? $data['request_time'] : null;
        $this->container['partner_code'] = isset($data['partner_code']) ? $data['partner_code'] : null;
        $this->container['acc_name'] = isset($data['acc_name']) ? $data['acc_name'] : null;
        $this->container['collect_amount'] = isset($data['collect_amount']) ? $data['collect_amount'] : null;
        $this->container['order_id'] = isset($data['order_id']) ? $data['order_id'] : null;
        $this->container['expire_date'] = isset($data['expire_date']) ? $data['expire_date'] : null;
        $this->container['bank'] = isset($data['bank']) ? $data['bank'] : null;
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
     * Gets request_id
     *
     * @return string
     */
    public function getRequestId()
    {
        return $this->container['request_id'];
    }

    /**
     * Sets request_id
     *
     * @param string $request_id Unique code
     *
     * @return $this
     */
    public function setRequestId($request_id)
    {
        $this->container['request_id'] = $request_id;

        return $this;
    }

    /**
     * Gets request_time
     *
     * @return string
     */
    public function getRequestTime()
    {
        return $this->container['request_time'];
    }

    /**
     * Sets request_time
     *
     * @param string $request_time Time send the request from PARTNER , format: YYYY-MM-DD HH:MM:SS.
     *
     * @return $this
     */
    public function setRequestTime($request_time)
    {
        $this->container['request_time'] = $request_time;

        return $this;
    }

    /**
     * Gets partner_code
     *
     * @return string
     */
    public function getPartnerCode()
    {
        return $this->container['partner_code'];
    }

    /**
     * Sets partner_code
     *
     * @param string $partner_code Unique code BAOKIM provide
     *
     * @return $this
     */
    public function setPartnerCode($partner_code)
    {
        $this->container['partner_code'] = $partner_code;

        return $this;
    }

    /**
     * Gets acc_name
     *
     * @return string
     */
    public function getAccName()
    {
        return $this->container['acc_name'];
    }

    /**
     * Sets acc_name
     *
     * @param string $acc_name The name of Account holder (name of USER)
     *
     * @return $this
     */
    public function setAccName($acc_name)
    {
        $this->container['acc_name'] = $acc_name;

        return $this;
    }

    /**
     * Gets collect_amount
     *
     * @return float
     */
    public function getCollectAmount()
    {
        return $this->container['collect_amount'];
    }

    /**
     * Sets collect_amount
     *
     * @param float $collect_amount collect amount
     *
     * @return $this
     */
    public function setCollectAmount($collect_amount)
    {
        $this->container['collect_amount'] = $collect_amount;

        return $this;
    }

    /**
     * Gets order_id
     *
     * @return string
     */
    public function getOrderId()
    {
        return $this->container['order_id'];
    }

    /**
     * Sets order_id
     *
     * @param string $order_id Unique id for each VA
     *
     * @return $this
     */
    public function setOrderId($order_id)
    {
        $this->container['order_id'] = $order_id;

        return $this;
    }

    /**
     * Gets expire_date
     *
     * @return string
     */
    public function getExpireDate()
    {
        return $this->container['expire_date'];
    }

    /**
     * Sets expire_date
     *
     * @param string $expire_date Expire date. Format: YYYYMM-DD HH:II:SS
     *
     * @return $this
     */
    public function setExpireDate($expire_date)
    {
        $this->container['expire_date'] = $expire_date;

        return $this;
    }

    /**
     * Gets bank
     *
     * @return string
     */
    public function getBank()
    {
        return $this->container['bank'];
    }

    /**
     * Sets bank
     *
     * @param string $bank Bank
     *
     * @return $this
     */
    public function setBank($bank)
    {
        $this->container['bank'] = $bank;

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
