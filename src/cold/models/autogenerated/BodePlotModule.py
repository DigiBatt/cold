
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPlotModule import ElectrochemicalPlot







class BodePlot(ElectrochemicalPlot):
    """
    Class representing the `BodePlot` entity, which inherits from:
    - ElectrochemicalPlot

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e0b57b09_68ee_4687_a901_bfb599421972'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BodePlot'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BodePlot(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e0b57b09_68ee_4687_a901_bfb599421972',
    
    class_name='BodePlot',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e0b57b09_68ee_4687_a901_bfb599421972',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BodePlot',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    