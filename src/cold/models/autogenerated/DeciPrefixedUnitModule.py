
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIMetricSubMultipleUnitModule import SIMetricSubMultipleUnit





from .MetricPrefixModule import MetricPrefix





class DeciPrefixedUnit(SIMetricSubMultipleUnit):
    """
    Class representing the `DeciPrefixedUnit` entity, which inherits from:
    - SIMetricSubMultipleUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1181c938_c8f0_4ad6_bc7a_2bfdc0903d29'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DeciPrefixedUnit'`
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
    obj = DeciPrefixedUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_1181c938_c8f0_4ad6_bc7a_2bfdc0903d29',
    
    class_name='DeciPrefixedUnit',
    
    hasMetricPrefix="example_value",
    
    hasPrefixMultiplier="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1181c938_c8f0_4ad6_bc7a_2bfdc0903d29',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DeciPrefixedUnit',
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
    
    

    

    