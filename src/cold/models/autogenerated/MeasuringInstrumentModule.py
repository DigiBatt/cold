
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasurerModule import Measurer







class MeasuringInstrument(Measurer):
    """
    Class representing the `MeasuringInstrument` entity, which inherits from:
    - Measurer

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f2d5d3ad_2e00_417f_8849_686f3988d929'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MeasuringInstrument'`
        - **Alias**: `class_name`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MeasuringInstrument(
    
    class_iri='https://w3id.org/emmo#EMMO_f2d5d3ad_2e00_417f_8849_686f3988d929',
    
    class_name='MeasuringInstrument',
    
    VIMTerm="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f2d5d3ad_2e00_417f_8849_686f3988d929',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MeasuringInstrument',
        alias="class_name"
    )
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    