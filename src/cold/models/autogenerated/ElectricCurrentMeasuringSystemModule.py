
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WholeModule import Whole



from .MeasuringSystemModule import MeasuringSystem



from .ObjectModule import Object





from .ConstituentModule import Constituent





class ElectricCurrentMeasuringSystem(Whole, MeasuringSystem, Object):
    """
    Class representing the `ElectricCurrentMeasuringSystem` entity, which inherits from:
    - Whole, MeasuringSystem, Object

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f693b744_930c_42ac_8e6f_627b22c6da3f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricCurrentMeasuringSystem'`
        - **Alias**: `class_name`
    
    - `hasConstituent` (`Optional[Constituent]`): 
        - **Default Value**: `None`
        - **Alias**: `hasConstituent`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricCurrentMeasuringSystem(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f693b744_930c_42ac_8e6f_627b22c6da3f',
    
    class_name='ElectricCurrentMeasuringSystem',
    
    hasConstituent="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f693b744_930c_42ac_8e6f_627b22c6da3f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricCurrentMeasuringSystem',
        alias="class_name"
    )
    
    hasConstituent: Optional[Constituent] = Field(
        None,
        alias="hasConstituent"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    @validator("hasConstituent", pre=True, always=True)
    def validate_hasConstituent(cls, value):
        if value is not None and not isinstance(value, Constituent):
            raise ValueError(f"Field 'hasConstituent' must be an instance of 'Constituent' or its subclass.")
        return value
    
    

    

    