
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPlotModule import ElectrochemicalPlot







class ChargeTimePlot(ElectrochemicalPlot):
    """
    Class representing the `ChargeTimePlot` entity, which inherits from:
    - ElectrochemicalPlot

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_46676855_68b0_4096_ac6c_35400111d46d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargeTimePlot'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargeTimePlot(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_46676855_68b0_4096_ac6c_35400111d46d',
    
    class_name='ChargeTimePlot',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_46676855_68b0_4096_ac6c_35400111d46d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargeTimePlot',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    