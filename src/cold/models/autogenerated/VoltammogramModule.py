
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CurrentPotentialPlotModule import CurrentPotentialPlot







class Voltammogram(CurrentPotentialPlot):
    """
    Class representing the `Voltammogram` entity, which inherits from:
    - CurrentPotentialPlot

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bbae1ef4_0a95_4e7d_9932_1bf939129eef'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Voltammogram'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Voltammogram(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bbae1ef4_0a95_4e7d_9932_1bf939129eef',
    
    class_name='Voltammogram',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bbae1ef4_0a95_4e7d_9932_1bf939129eef',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Voltammogram',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    