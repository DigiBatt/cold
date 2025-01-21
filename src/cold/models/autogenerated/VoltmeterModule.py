
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasuringInstrumentModule import MeasuringInstrument







class Voltmeter(MeasuringInstrument):
    """
    Class representing the `Voltmeter` entity, which inherits from:
    - MeasuringInstrument

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1355816f_a2b5_4800_8001_fc888f5d6b1b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Voltmeter'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Voltmeter(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1355816f_a2b5_4800_8001_fc888f5d6b1b',
    
    class_name='Voltmeter',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1355816f_a2b5_4800_8001_fc888f5d6b1b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Voltmeter',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    