
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIMetricMultipleUnitModule import SIMetricMultipleUnit





from .MetricPrefixModule import MetricPrefix





class YottaPrefixedUnit(SIMetricMultipleUnit):
    """
    Class representing the `YottaPrefixedUnit` entity, which inherits from:
    - SIMetricMultipleUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e79c62ff_10ad_4ec0_baba_c19ddd4eaa11'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'YottaPrefixedUnit'`
        - **Alias**: `class_name`
    
    - `hasMetricPrefix` (`Optional[MetricPrefix]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMetricPrefix`
    
    - `hasPrefixMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasPrefixMultiplier`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = YottaPrefixedUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_e79c62ff_10ad_4ec0_baba_c19ddd4eaa11',
    
    class_name='YottaPrefixedUnit',
    
    hasMetricPrefix="example_value",
    
    hasPrefixMultiplier="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e79c62ff_10ad_4ec0_baba_c19ddd4eaa11',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'YottaPrefixedUnit',
        alias="class_name"
    )
    
    hasMetricPrefix: Optional[MetricPrefix] = Field(
        None,
        alias="hasMetricPrefix"
    )
    
    hasPrefixMultiplier: Optional[str] = Field(
        None,
        alias="hasPrefixMultiplier"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    

    
    @validator("hasMetricPrefix", pre=True, always=True)
    def validate_hasMetricPrefix(cls, value):
        if value is not None and not isinstance(value, MetricPrefix):
            raise ValueError(f"Field 'hasMetricPrefix' must be an instance of 'MetricPrefix' or its subclass.")
        return value
    
    

    

    