
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasurerModule import Measurer







class MeasuringSystem(Measurer):
    """
    Class representing the `MeasuringSystem` entity, which inherits from:
    - Measurer

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_7dea2572_ab42_45bd_9fd7_92448cec762a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MeasuringSystem'`
        - **Alias**: `class_name`
    
    - `hasPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasPart`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MeasuringSystem(
    
    class_iri='https://w3id.org/emmo#EMMO_7dea2572_ab42_45bd_9fd7_92448cec762a',
    
    class_name='MeasuringSystem',
    
    hasPart="example_value",
    
    VIMTerm="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_7dea2572_ab42_45bd_9fd7_92448cec762a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MeasuringSystem',
        alias="class_name"
    )
    
    hasPart: Optional[str] = Field(
        None,
        alias="hasPart"
    )
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    