
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeviceModule import Device



from .ElectrochemicalCellModule import ElectrochemicalCell





from .ConstituentModule import Constituent



from .CaseModule import Case





class ElectrochemicalDevice(Device, ElectrochemicalCell):
    """
    Class representing the `ElectrochemicalDevice` entity, which inherits from:
    - Device, ElectrochemicalCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0acd0fc2_1048_4604_8e90_bf4e84bd87df'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalDevice'`
        - **Alias**: `class_name`
    
    - `figure` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `figure`
    
    - `hasConstituent` (`Optional[Constituent]`): 
        - **Default Value**: `None`
        - **Alias**: `hasConstituent`
    
    - `hasCase` (`Optional[Case]`): 
        - **Default Value**: `None`
        - **Alias**: `hasCase`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `custom_feature` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `customFeature`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalDevice(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0acd0fc2_1048_4604_8e90_bf4e84bd87df',
    
    class_name='ElectrochemicalDevice',
    
    figure="example_value",
    
    hasConstituent="example_value",
    
    hasCase="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    custom_feature=None,
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0acd0fc2_1048_4604_8e90_bf4e84bd87df',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalDevice',
        alias="class_name"
    )
    
    figure: Optional[str] = Field(
        None,
        alias="figure"
    )
    
    hasConstituent: Optional[Constituent] = Field(
        None,
        alias="hasConstituent"
    )
    
    hasCase: Optional[Case] = Field(
        None,
        alias="hasCase"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    custom_feature: Optional[str] = Field(
        None,
        alias="customFeature"
    )
    

    
    @validator("hasConstituent", pre=True, always=True)
    def validate_hasConstituent(cls, value):
        if value is not None and not isinstance(value, Constituent):
            raise ValueError(f"Field 'hasConstituent' must be an instance of 'Constituent' or its subclass.")
        return value
    
    @validator("hasCase", pre=True, always=True)
    def validate_hasCase(cls, value):
        if value is not None and not isinstance(value, Case):
            raise ValueError(f"Field 'hasCase' must be an instance of 'Case' or its subclass.")
        return value
    
    

    

    