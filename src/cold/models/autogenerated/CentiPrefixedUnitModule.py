
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIMetricSubMultipleUnitModule import SIMetricSubMultipleUnit





from .MetricPrefixModule import MetricPrefix





class CentiPrefixedUnit(SIMetricSubMultipleUnit):
    """
    Class representing the `CentiPrefixedUnit` entity, which inherits from:
    - SIMetricSubMultipleUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b55cd09a_e54d_4eb1_81dd_03c29d1b878e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CentiPrefixedUnit'`
        - **Alias**: `class_name`
    
    - `hasMetricPrefix` (`Optional[MetricPrefix]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMetricPrefix`
    
    - `hasPrefixMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasPrefixMultiplier`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CentiPrefixedUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_b55cd09a_e54d_4eb1_81dd_03c29d1b878e',
    
    class_name='CentiPrefixedUnit',
    
    hasMetricPrefix="example_value",
    
    hasPrefixMultiplier="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b55cd09a_e54d_4eb1_81dd_03c29d1b878e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CentiPrefixedUnit',
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
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasMetricPrefix", pre=True, always=True)
    def validate_hasMetricPrefix(cls, value):
        if value is not None and not isinstance(value, MetricPrefix):
            raise ValueError(f"Field 'hasMetricPrefix' must be an instance of 'MetricPrefix' or its subclass.")
        return value
    
    

    

    